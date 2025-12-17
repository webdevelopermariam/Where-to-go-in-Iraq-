
import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Iraq Tourism Recommender",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Cairo', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e22ce 100%);
    }
    
    .stApp {
        background: transparent;
    }
    
    h1, h2, h3 {
        color: Black !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 15px 30px;
        border-radius: 12px;
        border: none;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.6);
    }
    
    .recommendation-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        margin: 15px 0;
        transition: all 0.3s;
        border-left: 5px solid #10b981;
    }
    
    .recommendation-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .metric-value {
        font-size: 36px;
        font-weight: bold;
        color: #1e3c72;
    }
    
    .metric-label {
        font-size: 14px;
        color: #666;
        margin-top: 5px;
    }
    
    .score-badge {
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        box-shadow: 0 2px 10px rgba(16, 185, 129, 0.3);
    }
    
    .stSelectbox label, .stSlider label {
        color: Black !important;
        font-weight: 600;
        font-size: 16px;
    }
    
    .hero-section {
        background: rgba(255, 255, 255, 0.95);
        padding: 40px;
        border-radius: 20px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    .hero-title {
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(90deg, #1e3c72 0%, #7e22ce 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        font-size: 20px;
        color: #666;
    }
    
    .block-container h1 a, 
    .block-container h2 a, 
    .block-container h3 a, 
    .block-container h4 a {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_pickle_files():
    """Load pre-trained model files"""
    try:
        with open('tourism_data.pkl', 'rb') as f:
            data = pickle.load(f)
        with open('similarity_matrix.pkl', 'rb') as f:
            similarity = pickle.load(f)
        with open('table_info.pkl', 'rb') as f:
            table_info = pickle.load(f)
        return data, similarity, table_info, None
    except FileNotFoundError as e:
        return None, None, None, f"File not found: {e}. Please run prepare_ml_model.py first."
    except Exception as e:
        return None, None, None, str(e)

def get_item_display_name(item):
    """Get display name for an item"""
    name = item.get('name_english', 'Unknown')
    city = item.get('city', 'Unknown')
    return f"{name} ({city})"

def get_category_emoji(category):
    """Get emoji for category"""
    emojis = {
        'cafe': '📍',
        'hotel': '📍',
        'holy_place': '📍',
        'archaeological': '📍'
    }
    return emojis.get(category, '📍')

def recommend_similar(item_index, data, similarity, num_recs=5):
    """Get similar recommendations"""
    distances = sorted(
        list(enumerate(similarity[item_index])),
        reverse=True,
        key=lambda x: x[1]
    )
    
    recommendations = []
    for i in distances[1:num_recs+1]:
        item = data.iloc[i[0]]
        recommendations.append({
            'item': item,
            'similarity': i[1],
            'index': i[0]
        })
    
    return recommendations

def display_recommendation_card(rec, index):
    """Display a beautiful recommendation card"""
    item = rec['item']
    similarity = rec['similarity']
    name = item.get('name_english', 'Unknown')
    location = item.get('city', 'Unknown')
    category = item['category_type'].replace('_', ' ').title()
    emoji = get_category_emoji(item['category_type'])
    
    card_html = f"""
    <div class="recommendation-card">
        <h3>{emoji} {index}. {name}</h3>
        <p><strong>📍 Location:</strong> {location}</p>
        <p><strong>🏷️ Type:</strong> {category}</p>
    """
    
    if pd.notna(item.get('category')):
        card_html += f"<p><strong>✨ Category:</strong> {item['category']}</p>"
    
    if pd.notna(item.get('price_range')):
        card_html += f"<p><strong>💰 Price Range:</strong> {item['price_range']}</p>"
    
    if pd.notna(item.get('rating')):
        card_html += f"<p><strong>⭐ Rating:</strong> {item['rating']}</p>"
    
    if pd.notna(item.get('best_for')):
        card_html += f"<p><strong>🎯 Best For:</strong> {item['best_for']}</p>"
    
    match_pct = int(similarity * 100)
    card_html += f'<p style="margin-top: 15px;"><span class="score-badge">🎯 Match: {match_pct}%</span></p>'
    
    map_link = item.get('google_maps_link')
    if pd.notna(map_link):
        card_html += f'<p style="margin-top: 10px;"><a href="{map_link}" target="_blank" style="color: #10b981; text-decoration: none; font-weight: bold;">🗺️ View on Google Maps →</a></p>'
    
    card_html += "</div>"
    
    st.markdown(card_html, unsafe_allow_html=True)

def main():
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">Iraq Tourism Recommender</div>
        <div class="hero-subtitle">Discover the Perfect Places Recommendations</div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.spinner("🤖 Loading Recommendation Engine..."):
        data, similarity, table_info, error = load_pickle_files()
    
    if error:
        st.error(f"❌ Error loading model files: {error}")
        st.info("💡 Please run `python prepare_ml_model.py` first to generate the model files.")
        return
    
    st.markdown("###  Available Places")
    cols = st.columns(len(table_info) + 1)
    
    with cols[0]:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(data)}</div>
            <div class="metric-label">Total Places</div>
        </div>
        """, unsafe_allow_html=True)
    
    for idx, (table_name, category, count) in enumerate(table_info, 1):
        emoji = get_category_emoji(category)
        with cols[idx]:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{emoji} {count}</div>
                <div class="metric-label">{category.replace('_', ' ').title()}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("## 🎯 Find Your Perfect Destination")
    
    data['display_name'] = data.apply(get_item_display_name, axis=1)
    items_list = data['display_name'].tolist()
    
    with st.sidebar:
        st.markdown("###  Customize Your Search")
        
        categories = ['All'] + [info[1].replace('_', ' ').title() for info in table_info]
        selected_category = st.selectbox("Filter by Category", categories)
        
        num_recs = st.slider("Number of Recommendations", 3, 10, 5)
        
        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.info("""
        Wondering where to go next in Iraq? Let us help you discover amazing places tailored to your interests!
        """)
    
    if selected_category != 'All':
        category_key = selected_category.lower().replace(' ', '_')
        filtered_data = data[data['category_type'] == category_key]
        if not filtered_data.empty:
            items_list = filtered_data['display_name'].tolist()
    
    selected_item = st.selectbox(
        "🔍 Select a place you like:",
        items_list,
        help="Choose a place and we'll find similar ones for you!"
    )
    
    if st.button(" Get Recommendations", use_container_width=True):
        
        with st.spinner("finding similar places..."):
            selected_row = data[data['display_name'] == selected_item].iloc[0]
            selected_index = data[data['display_name'] == selected_item].index[0]
            
            recommendations = recommend_similar(selected_index, data, similarity, num_recs)
            
            st.success(f"✅ Found {len(recommendations)} similar places!")
            
            st.markdown("###  You Selected:")
            with st.expander("View Details", expanded=True):
                col1, col2 = st.columns([1, 2])
                with col1:
                    emoji = get_category_emoji(selected_row['category_type'])
                    st.markdown(f"## {emoji}")
                with col2:
                    st.markdown(f"**{selected_row.get('name_english')}**")
                    st.caption(f"📍 {selected_row.get('city')}")
                    st.caption(f"🏷️ {selected_row['category_type'].replace('_', ' ').title()}")
            
            st.markdown("---")
            st.markdown("###  Similar Places You Might Like:")
            
            for idx, rec in enumerate(recommendations, 1):
                display_recommendation_card(rec, idx)
    
    st.markdown("---")

if __name__ == "__main__":
    main()