import streamlit as st
from google import genai
from PIL import Image

# --- CONFIGURATION ---
# Replace with your actual AIza key
client = genai.Client(api_key="write your API key here")

# --- SYSTEM PROMPT ---
sys_instruct = """
You are 'AgriGuard', an expert AI Agronomist. 
1. ANALYZE the plant image for pests, diseases, or nutrient stress.
2. IDENTIFY the specific issue (e.g., Fall Armyworm, Late Blight, Nitrogen Deficiency).
3. EXPLAIN the lifecycle stage (Larva, Pupa, Adult) or disease progression.
4. RECOMMEND TREATMENT (Must include both):
   - Organic: (e.g., Neem oil, predatory insects, crop rotation).
   - Chemical: (Specific dosage, safety warnings).
5. STRATEGY: Suggest a long-term IPM (Integrated Pest Management) plan.
"""

# --- APP UI ---
st.title("🌱 AgriGuard: AI Agronomist")
st.write("Powered by Google Gemini 2.5 • Kshitij 2026")

uploaded_file = st.file_uploader(
    "Upload a leaf photo...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Field Image', use_column_width=True)

    if st.button("Diagnose Crop"):
        with st.spinner('AgriGuard is analyzing plant health...'):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[sys_instruct, image]
                )
                st.markdown("### 📋 Diagnosis Report")
                st.markdown(response.text)
                st.success("Analysis Complete.")
            except Exception as e:
                st.error(f"Connection Error: {e}")
