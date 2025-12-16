import mysql.connector
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HOST = "localhost"
DATABASE = "info"
USER = "root"
PASSWORD = "Maryam-200511"

def connect_to_db():
    """Connect to MySQL database"""
    try:
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            charset='utf8mb4'
        )
        print("✓ Connected to database")
        return conn
    except Exception as e:
        print(f"✗ Database error: {e}")
        return None

def load_all_data():
    """Load all tourism data from MySQL"""
    conn = connect_to_db()
    if not conn:
        return None
    
    print("\nLoading data from database...")
    
    dfs = []
    table_info = []
    
    tables = [
        ("cafes", "cafes"),
        ("hotels", "hotels"),
        ("`holy-Places`", "holy-Places"),
        ("`archaeological Site`", "archaeological site")
    ]
    
    for table_name, category in tables:
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name}", con=conn)
            if not df.empty:
                df['category_type'] = category  
                dfs.append(df)
                print(f"   ✓ {table_name}: {len(df)} records")
                table_info.append((table_name, category, len(df)))
            else:
                print(f"   ✗ {table_name}: No data")
        except Exception as e:
            print(f"   ✗ {table_name}: {e}")
    
    conn.close()
    
    if not dfs:
        print("\n✗ No data loaded from any table!")
        return None
    
    data = pd.concat(dfs, ignore_index=True)
    print(f"\n✓ Total records loaded: {len(data)}")
    
    return data, table_info

def create_combined_features(row):
    """Create a combined text feature from all relevant columns"""
    features = []
    
    if pd.notna(row.get('name_english')):
        features.append(str(row['name_english']) * 3)
    
    if pd.notna(row.get('city')):
        features.append(str(row['city']) * 2)
    
    if pd.notna(row.get('category')):
        features.append(str(row['category']))
    
    if pd.notna(row.get('best_for')):
        features.append(str(row['best_for']))
    
    if pd.notna(row.get('price_range')):
        features.append(str(row['price_range']))
    
    if pd.notna(row.get('category_type')):
        features.append(str(row['category_type']) * 2)
    
    return ' '.join(features)

def prepare_recommendation_model():
    """Prepare and save the recommendation model"""
    
    print("\n" + "="*70)
    print(" PREPARING ML RECOMMENDATION MODEL")
    print("="*70)
    
    result = load_all_data()
    if result is None:
        print("\n✗ Failed to load data. Exiting.")
        return
    
    data, table_info = result
    
    print("\n Creating feature vectors...")
    data['combined_features'] = data.apply(create_combined_features, axis=1)
    
    original_count = len(data)
    data = data[data['combined_features'].str.strip() != '']
    print(f"   ✓ Records with features: {len(data)} (removed {original_count - len(data)} empty)")
    
    if len(data) == 0:
        print("\n✗ No valid features created. Check your data columns.")
        return
    
    print("\n Computing TF-IDF vectors...")
    tfidf = TfidfVectorizer(
        max_features=5000,
        stop_words='english',        ngram_range=(1, 2),
        min_df=1,
        max_df=0.8
    )
    
    tfidf_matrix = tfidf.fit_transform(data['combined_features'])
    print(f"   ✓ TF-IDF Matrix shape: {tfidf_matrix.shape}")
    print(f"   ✓ Vocabulary size: {len(tfidf.vocabulary_)}")
    
    print("\n Computing similarity matrix...")
    similarity_matrix = cosine_similarity(tfidf_matrix)
    print(f"   ✓ Similarity Matrix shape: {similarity_matrix.shape}")
    
    data = data.reset_index(drop=True)
    
    print("\nSaving model files...")
    
    try:
        with open('tourism_data.pkl', 'wb') as f:
            pickle.dump(data, f)
        print("   ✓ tourism_data.pkl saved")
        
        with open('similarity_matrix.pkl', 'wb') as f:
            pickle.dump(similarity_matrix, f)
        print("   ✓ similarity_matrix.pkl saved")
        
        with open('tfidf_vectorizer.pkl', 'wb') as f:
            pickle.dump(tfidf, f)
        print("   ✓ tfidf_vectorizer.pkl saved")
        
        with open('table_info.pkl', 'wb') as f:
            pickle.dump(table_info, f)
        print("   ✓ table_info.pkl saved")
    except Exception as e:
        print(f"\n✗ Error saving files: {e}")
        return
    
    print("\n" + "="*70)
    print("MODEL PREPARATION COMPLETE!")
    print("="*70)
    
    print("\n Summary:")
    print(f"   • Total places: {len(data)}")
    for table_name, category, count in table_info:
        print(f"   • {category.replace('_', ' ').title()}: {count}")
    
    print("\n Next step:")
    print("   Run: streamlit run web_app.py")
    
    return data, similarity_matrix

if __name__ == "__main__":
    try:
        prepare_recommendation_model()
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()