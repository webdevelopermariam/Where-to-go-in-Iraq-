import gspread
from google.oauth2.service_account import Credentials
import mysql.connector as mysql
import logging
import sys
import time

logging.basicConfig(
    filename='.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

HOST = ""
DATABASE = ""
USER = ""
PASSWORD = ""

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
Sheet_ID = ""

FORCE_TRANSFER = '--force' in sys.argv or '-f' in sys.argv

def connect_to_db():
    try:
        con = mysql.connect(
            host=HOST, 
            database=DATABASE, 
            user=USER, 
            password=PASSWORD,
            charset='utf8mb4'
        )
        return con
    except mysql.Error as err:
        logging.error(f"Error connecting to database: {err}")
        print(f"Error connecting to database: {err}")
        return None

def connect_to_sheet():
    try:
        creds = Credentials.from_service_account_file(
            ".json",
            scopes=SCOPES
        )
        client = gspread.authorize(creds)
        workbook = client.open_by_key(Sheet_ID)
        print(f"Worksheets available: {[ws.title for ws in workbook.worksheets()]}")
        return workbook
    except Exception as err:
        logging.error(f"Error connecting to Google Sheet: {err}")
        print(f"Error connecting to Google Sheet: {err}")
        return None

def safe_get_value(row, idx, default=''):
    """Safely get value from row at index, return default if None or out of bounds"""
    if idx is None:
        return default
    if idx < len(row):
        return row[idx]
    return default

def transfer_hotels(db_con, sheet):
    """Transfer Hotels data"""
    try:
        cursor = db_con.cursor()
        all_data = sheet.get_all_values()
        
        if len(all_data) <= 1:
            print("No data in Hotels sheet")
            return 0
        
        headers = [h.strip() for h in all_data[0]]
        rows = all_data[1:]
        
        print(f"Hotels columns: {headers}")
        
        location_id_idx = next((i for i, h in enumerate(headers) if 'location' in h.lower() and 'id' in h.lower()), None)
        name_idx = next((i for i, h in enumerate(headers) if 'name' in h.lower() and 'english' in h.lower()), None)
        city_idx = next((i for i, h in enumerate(headers) if 'city' in h.lower()), None)
        category_idx = next((i for i, h in enumerate(headers) if 'category' in h.lower()), None)
        price_idx = next((i for i, h in enumerate(headers) if 'price' in h.lower()), None)
        rating_idx = next((i for i, h in enumerate(headers) if 'rating' in h.lower()), None)
        best_for_idx = next((i for i, h in enumerate(headers) if 'best for' in h.lower()), None)
        maps_idx = next((i for i, h in enumerate(headers) if 'map' in h.lower() and 'link' in h.lower()), None)
        is_transferred_idx = next((i for i, h in enumerate(headers) if 'is_transfer' in h.lower()), None)
        
        if location_id_idx is None:
            print(f"ERROR: Could not find Location ID column in: {headers}")
            return 0
        
        insert_query = """
            INSERT INTO hotels (
                location_id, name_english, city, category, 
                price_range, rating, best_for, google_maps_link
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name_english = VALUES(name_english),
                city = VALUES(city),
                category = VALUES(category),
                price_range = VALUES(price_range),
                rating = VALUES(rating),
                best_for = VALUES(best_for),
                google_maps_link = VALUES(google_maps_link)
        """
        
        transferred = 0
        cells_to_update = []  
        
        for idx, row in enumerate(rows, start=2):
            if not row:
                continue
            
            if not FORCE_TRANSFER and is_transferred_idx is not None:
                transferred_val = safe_get_value(row, is_transferred_idx)
                if transferred_val.lower() in ['true', 'yes', '1']:
                    continue
            
            location_id = safe_get_value(row, location_id_idx)
            if not location_id.strip():
                continue
            
            row_data = (
                location_id,
                safe_get_value(row, name_idx),
                safe_get_value(row, city_idx),
                safe_get_value(row, category_idx),
                safe_get_value(row, price_idx),
                safe_get_value(row, rating_idx),
                safe_get_value(row, best_for_idx),
                safe_get_value(row, maps_idx)
            )
            
            cursor.execute(insert_query, row_data)
            transferred += 1
            
            if is_transferred_idx is not None:
                cells_to_update.append({
                    'range': f'{chr(65 + is_transferred_idx)}{idx}',
                    'values': [['TRUE']]
                })
        
        db_con.commit()
        cursor.close()
        
        if cells_to_update:
            sheet.batch_update(cells_to_update)
            print(f"   200 Updated {len(cells_to_update)} is_transferred flags")
        
        return transferred
        
    except Exception as err:
        logging.error(f"Error transferring hotels: {err}")
        print(f"Error transferring hotels: {err}")
        import traceback
        traceback.print_exc()
        return 0

def transfer_cafes(db_con, sheet):
    """Transfer Cafes data"""
    try:
        cursor = db_con.cursor()
        all_data = sheet.get_all_values()
        
        if len(all_data) <= 1:
            print("No data in Cafes sheet")
            return 0
        
        headers = [h.strip() for h in all_data[0]]
        rows = all_data[1:]
        
        print(f"Cafes columns: {headers}")
        
        location_id_idx = next((i for i, h in enumerate(headers) if 'location' in h.lower() and 'id' in h.lower()), None)
        name_idx = next((i for i, h in enumerate(headers) if 'name' in h.lower() and 'english' in h.lower()), None)
        city_idx = next((i for i, h in enumerate(headers) if 'city' in h.lower()), None)
        category_idx = next((i for i, h in enumerate(headers) if 'category' in h.lower()), None)
        rating_idx = next((i for i, h in enumerate(headers) if 'rating' in h.lower()), None)
        price_idx = next((i for i, h in enumerate(headers) if 'price' in h.lower()), None)
        best_for_idx = next((i for i, h in enumerate(headers) if 'best for' in h.lower()), None)
        maps_idx = next((i for i, h in enumerate(headers) if 'map' in h.lower()), None)
        is_transferred_idx = next((i for i, h in enumerate(headers) if 'is_transfer' in h.lower()), None)
        
        if name_idx is None:
            print(f"ERROR: 'Name' column not found. Available columns: {headers}")
            return 0
        
        insert_query = """
            INSERT INTO cafes (
                location_id, name_english, city, category,
                rating, price_range, best_for, google_maps_link
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name_english = VALUES(name_english),
                city = VALUES(city),
                category = VALUES(category),
                rating = VALUES(rating),
                price_range = VALUES(price_range),
                best_for = VALUES(best_for),
                google_maps_link = VALUES(google_maps_link)
        """
        
        transferred = 0
        cells_to_update = []
        
        for idx, row in enumerate(rows, start=2):
            if not row:
                continue
            
            if not FORCE_TRANSFER and is_transferred_idx is not None:
                transferred_val = safe_get_value(row, is_transferred_idx)
                if transferred_val.lower() in ['true', 'yes', '1']:
                    continue
            
            name = safe_get_value(row, name_idx)
            location_id = safe_get_value(row, location_id_idx)
            
            if not name.strip() and not location_id.strip():
                continue
            
            row_data = (
                location_id,
                name,
                safe_get_value(row, city_idx),
                safe_get_value(row, category_idx),
                safe_get_value(row, rating_idx),
                safe_get_value(row, price_idx),
                safe_get_value(row, best_for_idx),
                safe_get_value(row, maps_idx)
            )
            
            cursor.execute(insert_query, row_data)
            transferred += 1
            
            if is_transferred_idx is not None:
                cells_to_update.append({
                    'range': f'{chr(65 + is_transferred_idx)}{idx}',
                    'values': [['TRUE']]
                })
        
        db_con.commit()
        cursor.close()
        
        if cells_to_update:
            sheet.batch_update(cells_to_update)
            print(f"   200 Updated {len(cells_to_update)} is_transferred flags")
        
        return transferred
        
    except Exception as err:
        logging.error(f"Error transferring cafes: {err}")
        print(f"Error transferring cafes: {err}")
        import traceback
        traceback.print_exc()
        return 0

def transfer_holy_places(db_con, sheet):
    """Transfer Holy-Places data"""
    try:
        cursor = db_con.cursor()
        all_data = sheet.get_all_values()
        
        if len(all_data) <= 1:
            print("No data in Holy-Places sheet")
            return 0
        
        headers = [h.strip() for h in all_data[0]]
        rows = all_data[1:]
        
        print(f"Holy-Places columns: {headers}")
        
        location_id_idx = next((i for i, h in enumerate(headers) if h.lower() == 'id'), None)
        name_idx = next((i for i, h in enumerate(headers) if 'name' in h.lower() and 'english' in h.lower()), None)
        city_idx = next((i for i, h in enumerate(headers) if 'city' in h.lower()), None)
        category_idx = next((i for i, h in enumerate(headers) if 'category' in h.lower()), None)
        rating_idx = next((i for i, h in enumerate(headers) if 'rating' in h.lower()), None)
        price_idx = next((i for i, h in enumerate(headers) if 'price' in h.lower()), None)
        best_for_idx = next((i for i, h in enumerate(headers) if 'best for' in h.lower()), None)
        maps_idx = next((i for i, h in enumerate(headers) if 'map' in h.lower() and 'link' in h.lower()), None)
        is_transferred_idx = next((i for i, h in enumerate(headers) if 'is_transfer' in h.lower()), None)
        
        if location_id_idx is None:
            print(f"ERROR: 'ID' column not found. Available columns: {headers}")
            return 0
        
        insert_query = """
            INSERT INTO `holy-places` (
                location_id, name_english, city, category, 
                price_range, rating, best_for, google_maps_link
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name_english = VALUES(name_english),
                city = VALUES(city),
                category = VALUES(category),
                price_range = VALUES(price_range),
                rating = VALUES(rating),
                best_for = VALUES(best_for),
                google_maps_link = VALUES(google_maps_link)
        """
        
        transferred = 0
        cells_to_update = []
        
        for idx, row in enumerate(rows, start=2):
            if not row:
                continue
            
            if not FORCE_TRANSFER and is_transferred_idx is not None:
                transferred_val = safe_get_value(row, is_transferred_idx)
                if transferred_val.lower() in ['true', 'yes', '1']:
                    continue
            
            location_id = safe_get_value(row, location_id_idx)
            if not location_id.strip():
                continue
            
            row_data = (
                location_id,
                safe_get_value(row, name_idx),
                safe_get_value(row, city_idx),
                safe_get_value(row, category_idx),
                safe_get_value(row, price_idx),
                safe_get_value(row, rating_idx),
                safe_get_value(row, best_for_idx),
                safe_get_value(row, maps_idx)
            )
            
            cursor.execute(insert_query, row_data)
            transferred += 1
            
            if is_transferred_idx is not None:
                cells_to_update.append({
                    'range': f'{chr(65 + is_transferred_idx)}{idx}',
                    'values': [['TRUE']]
                })
        
        db_con.commit()
        cursor.close()
        
        if cells_to_update:
            sheet.batch_update(cells_to_update)
            print(f"   200 Updated {len(cells_to_update)} is_transferred flags")
        
        return transferred
        
    except Exception as err:
        logging.error(f"Error transferring holy places: {err}")
        print(f"Error transferring holy places: {err}")
        import traceback
        traceback.print_exc()
        return 0

def transfer_archaeological_sites(db_con, sheet):
    """Transfer Archaeological Site data"""
    try:
        cursor = db_con.cursor()
        all_data = sheet.get_all_values()
        
        if len(all_data) <= 1:
            print("No data in Archaeological Site sheet")
            return 0
        
        headers = [h.strip() for h in all_data[0]]
        rows = all_data[1:]
        
        print(f"Archaeological Site columns: {headers}")
        
        location_id_idx = next((i for i, h in enumerate(headers) if h.lower() == 'id'), None)
        name_idx = next((i for i, h in enumerate(headers) if 'name' in h.lower() and 'english' in h.lower()), None)
        city_idx = next((i for i, h in enumerate(headers) if 'city' in h.lower() or 'region' in h.lower()), None)
        category_idx = next((i for i, h in enumerate(headers) if 'category' in h.lower()), None)
        rating_idx = next((i for i, h in enumerate(headers) if 'rating' in h.lower()), None)
        price_idx = next((i for i, h in enumerate(headers) if 'price' in h.lower()), None)
        best_for_idx = next((i for i, h in enumerate(headers) if 'best for' in h.lower()), None)
        maps_idx = next((i for i, h in enumerate(headers) if 'map' in h.lower() and 'link' in h.lower()), None)
        is_transferred_idx = next((i for i, h in enumerate(headers) if 'is_transfer' in h.lower()), None)
        
        if location_id_idx is None:
            print(f"ERROR: 'ID' column not found. Available columns: {headers}")
            return 0
        
        insert_query = """
            INSERT INTO `archaeological site` (
                location_id, name_english, city, category,
                price_range, rating, best_for, google_maps_link
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name_english = VALUES(name_english),
                city = VALUES(city),
                category = VALUES(category),
                price_range = VALUES(price_range),
                rating = VALUES(rating),
                best_for = VALUES(best_for),
                google_maps_link = VALUES(google_maps_link)
        """
        
        transferred = 0
        cells_to_update = []
        
        for idx, row in enumerate(rows, start=2):
            if not row:
                continue
            
            if not FORCE_TRANSFER and is_transferred_idx is not None:
                transferred_val = safe_get_value(row, is_transferred_idx)
                if transferred_val.lower() in ['true', 'yes', '1']:
                    continue
            
            location_id = safe_get_value(row, location_id_idx)
            if not location_id.strip():
                continue
            
            row_data = (
                location_id,
                safe_get_value(row, name_idx),
                safe_get_value(row, city_idx),
                safe_get_value(row, category_idx),
                safe_get_value(row, price_idx),
                safe_get_value(row, rating_idx),
                safe_get_value(row, best_for_idx),
                safe_get_value(row, maps_idx)
            )
            
            cursor.execute(insert_query, row_data)
            transferred += 1
            
            if is_transferred_idx is not None:
                cells_to_update.append({
                    'range': f'{chr(65 + is_transferred_idx)}{idx}',
                    'values': [['TRUE']]
                })
        
        db_con.commit()
        cursor.close()
        
        if cells_to_update:
            sheet.batch_update(cells_to_update)
            print(f"   200 Updated {len(cells_to_update)} is_transferred flags")
        
        return transferred
        
    except Exception as err:
        logging.error(f"Error transferring archaeological sites: {err}")
        print(f"Error transferring archaeological sites: {err}")
        import traceback
        traceback.print_exc()
        return 0

def transfer_all_data():
    """Transfer all sheets"""
    db_con = connect_to_db()
    workbook = connect_to_sheet()
    
    if not db_con or not workbook:
        print("Failed to connect")
        return
    
    print("\n" + "="*50)
    print("Starting data transfer...")
    if FORCE_TRANSFER:
        print("FORCE MODE: Re-transferring all records")
    print("="*50 + "\n")
    
    total_transferred = 0
    
    try:
        print("Processing Hotels...")
        hotels_sheet = workbook.worksheet("hotels") 
        count = transfer_hotels(db_con, hotels_sheet)
        print(f"[SUCCESS] Hotels: {count} records transferred\n")
        total_transferred += count
        time.sleep(2)  
    except Exception as e:
        print(f"[ERROR] Hotels sheet error: {e}\n")
    
    try:
        print("Processing Cafes...")
        cafes_sheet = workbook.worksheet("cafes")
        count = transfer_cafes(db_con, cafes_sheet)
        print(f"[SUCCESS] Cafes: {count} records transferred\n")
        total_transferred += count
        time.sleep(2)
    except Exception as e:
        print(f"[ERROR] Cafes sheet error: {e}\n")
    
    try:
        print("Processing Holy-Places...")
        holy_sheet = workbook.worksheet("holy-Places")  
        count = transfer_holy_places(db_con, holy_sheet)
        print(f"[SUCCESS] Holy-Places: {count} records transferred\n")
        total_transferred += count
        time.sleep(2)
    except Exception as e:
        print(f"[ERROR] Holy-Places sheet error: {e}\n")
    
    try:
        print("Processing Archaeological Site...")
        arch_sheet = workbook.worksheet("archaeological site")
        count = transfer_archaeological_sites(db_con, arch_sheet)
        print(f"[SUCCESS] Archaeological Site: {count} records transferred\n")
        total_transferred += count
    except Exception as e:
        print(f"[ERROR] Archaeological Site sheet error: {e}\n")
    
    db_con.close()
    
    print("="*50)
    print(f"COMPLETE: {total_transferred} total records transferred")
    print("="*50 + "\n")
    
    logging.info(f"Transfer completed: {total_transferred} total records")

if __name__ == "__main__":
    print("="*70)
    print("Google Sheets to MySQL Transfer Tool")
    print("="*70)
    print("Usage: python main.py [--force|-f]")
    print("  --force, -f : Force re-transfer all records (ignore is_transferred)")
    print("="*70 + "\n")
    
    print("Starting transfer process...")

    transfer_all_data()
