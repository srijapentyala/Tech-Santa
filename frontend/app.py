import streamlit as st
import requests
import base64
import os

# Configuration
API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(
    page_title="Problem Solver AI",
    page_icon="💡",
    layout="wide"
)

# Custom CSS for cards
st.markdown("""
<style>
    .category-badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 0.8em;
    }
    .solvable { background-color: #d4edda; color: #155724; }
    .unsolvable { background-color: #f8d7da; color: #721c24; }
</style>
""", unsafe_allow_html=True)

st.title("💡 AI Opportunity Compass")
st.caption("Transforming real-world pain points into actionable tech opportunities.")

# Layout
tab1, tab2 = st.tabs(["🚀 Submit Problem", "🔍 Explore Opportunities"])

# --- TAB 1: SUBMIT ---
with tab1:
    st.header("What's broken?")
    st.write("Submit a pain point you face. Our AI will analyze if it's a solvable software problem.")
    
    with st.form("submission_form"):
        description = st.text_area(
            "Describe the problem in detail:",
            height=150,
            placeholder="e.g., Farmers in my village struggle to identify crop diseases early..."
        )
        submitted = st.form_submit_button("Analyze & Submit")
        
        if submitted and description:
            with st.spinner("Consulting the AI Oracle..."):
                try:
                    response = requests.post(f"{API_URL}/submit", json={"description": description})
                    if response.status_code == 200:
                        data = response.json()
                        analysis = data.get("analysis", {})
                        
                        # Result Display
                        category = analysis.get('category', 'Unknown')
                        color_class = "solvable" if category == "Solvable" else "unsolvable"
                        
                        st.markdown(f"### Result: <span class='category-badge {color_class}'>{category}</span>", unsafe_allow_html=True)
                        
                        if category == "Solvable":
                            st.success(f"**Opportunity Found!**")
                            st.info(f"**Guidance:** {analysis.get('guidance')}")
                        else:
                            st.warning(f"**Status:** {category}")
                        
                        with st.expander("Why this category?"):
                            st.write(analysis.get("reasoning"))
                            
                    else:
                        st.error(f"Error: {response.text}")
                except Exception as e:
                    st.error(f"Connection failed: {e}")

# --- TAB 2: EXPLORE ---
with tab2:
    st.header("Open Opportunities")
    st.write("Browse validated problems ready for a solution.")
    
    # Fetch Data
    try:
        response = requests.get(f"{API_URL}/opportunities")
        if response.status_code == 200:
            opportunities = response.json()
            
            # --- SIDEBAR CONTROLS ---
            with st.sidebar:
                st.header("🔍 Filter & Sort")
                
                # Sort Controls
                sort_option = st.selectbox(
                    "Sort By",
                    ["Newest", "Most Liked", "Highest Impact"],
                    index=0
                )

                st.divider()
                st.subheader("Filters")

                # Filter: Industry
                all_industries = sorted(list(set(op['analysis'].get('industry', 'General') for op in opportunities)))
                selected_industry = st.multiselect("Industry", all_industries)

                # Filter: Difficulty
                all_difficulties = ["Low", "Medium", "High"]
                selected_diff = st.multiselect("Complexity", all_difficulties)

            # --- LOGIC ---
            
            # 1. Apply Filters
            if selected_industry:
                opportunities = [op for op in opportunities if op['analysis'].get('industry') in selected_industry]
            
            if selected_diff:
                opportunities = [op for op in opportunities if op.get('metrics', {}).get('difficulty', 'Medium') in selected_diff]

            # 2. Apply Sorting
            if sort_option == "Most Liked":
                opportunities.sort(key=lambda x: x.get('metrics', {}).get('likes', 0), reverse=True)
            elif sort_option == "Highest Impact":
                opportunities.sort(key=lambda x: x.get('metrics', {}).get('impact_score', 0), reverse=True)
            else: # Newest
                # Assuming the list comes sorted by date from backend, or strict parse
                pass 

            st.markdown(f"**Showing {len(opportunities)} opportunities**")
            st.markdown("---")
            
            # Grid Layout
            if not opportunities:
                st.info("No opportunities found matching your criteria.")
            
            for op in opportunities:
                analysis = op.get("analysis", {})
                metrics = op.get("metrics", {"likes": 0, "views": 0, "difficulty": "Medium", "impact_score": 0})
                
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        # Header with Metrics badges
                        st.subheader(analysis.get("summary"))
                        
                        # Metrics Row
                        m1, m2, m3, m4 = st.columns(4)
                        m1.caption(f"❤️ {metrics.get('likes')} Likes")
                        m2.caption(f"👀 {metrics.get('views')} Views")
                        m3.caption(f"⚡ Impact: {metrics.get('impact_score')}/100")
                        m4.caption(f"🏗️ Diff: {metrics.get('difficulty')}")

                        st.markdown(f"**Industry:** `{analysis.get('industry', 'General')}`")
                        st.markdown(f"> *\"{op.get('original_text')}\"*")
                        
                        with st.expander("🛠 Technical Guidance"):
                            st.write(analysis.get("guidance"))
                            st.caption(f"Reasoning: {analysis.get('reasoning')}")
                            
                    with col2:
                        # Audio Player
                        audio_b64 = op.get("audio_b64")
                        if audio_b64:
                            st.markdown("**🎧 Audio Summary**")
                            audio_bytes = base64.b64decode(audio_b64)
                            st.audio(audio_bytes, format="audio/mp3")
                        else:
                            st.caption("No audio available")
                            
                    st.divider()
                    
        else:
            st.error("Failed to fetch opportunities.")
    except Exception as e:
        st.error(f"Could not connect to backend: {e}")

