import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("cancer_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label = pickle.load(open("label.pkl","rb"))

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="wide"
)

with st.sidebar:
    st.sidebar.metric("Model Accuracy", "96.49%")
    st.header("🩺 Model Information")

    st.write("**Algorithm:** K-Nearest Neighbors (KNN)")
    st.write("**Dataset:** Breast Cancer Wisconsin Dataset")
    st.write("**Features:** 30")
    st.write("**Target:** Benign / Malignant")

    st.divider()

    st.info("Enter all 30 feature values and click Predict.")
    

st.title("🩺 Breast Cancer Prediction System")


st.markdown("""
### 📋 About This Application

This application predicts whether a breast tumor is **Benign** or **Malignant**
using a Machine Learning K-Nearest Neighbors (KNN) model.

Enter all the required medical measurements and click **Predict**.
""")

st.divider()

with st.expander("📊 Mean Feature", expanded = True):
    

     col1, col2 = st.columns(2)

with col1 : 
     radius_mean = st.number_input("Radius Mean", min_value=6.981, max_value=28.110, value=14.127, step=0.01)
     perimeter_mean = st.number_input("Perimeter Mean", min_value=43.790, max_value=188.500, value=91.969, step=0.1)
     smoothness_mean = st.number_input("Smoothness Mean", min_value=0.053, max_value=0.163, value=0.096, step=0.001)
     concavity_mean = st.number_input("Concavity Mean", min_value=0.000, max_value=0.427, value=0.089, step=0.001)
     symmetry_mean = st.number_input("Symmetry Mean", min_value=0.106, max_value=0.304, value=0.181, step=0.001)
    
with col2 :
    texture_mean = st.number_input("Texture Mean", min_value=9.710, max_value=39.280, value=19.290, step=0.01)
    area_mean = st.number_input("Area Mean", min_value=143.500, max_value=2501.000, value=654.889, step=1.0)
    compactness_mean = st.number_input("Compactness Mean", min_value=0.019, max_value=0.345, value=0.104, step=0.001)
    concave_points_mean = st.number_input("Concave Points Mean", min_value=0.000, max_value=0.201, value=0.049, step=0.001)
    fractal_dimension_mean = st.number_input("Fractal Dimension Mean", min_value=0.050, max_value=0.097, value=0.063, step=0.001)
    
with st.expander("📈  Standard Error (SE) Features"):
    
    col1, col2 = st.columns(2)
        
with col1 :    
     radius_se = st.number_input("Radius SE", min_value=0.112, max_value=2.873, value=0.405, step=0.01)
     perimeter_se = st.number_input("Perimeter SE", min_value=0.757, max_value=21.980, value=2.866, step=0.01)
     smoothness_se = st.number_input("Smoothness SE", min_value=0.002, max_value=0.031, value=0.007, step=0.001)
     concavity_se = st.number_input("Concavity SE", min_value=0.000, max_value=0.396, value=0.032, step=0.001)
     symmetry_se = st.number_input("Symmetry SE", min_value=0.008, max_value=0.079, value=0.021, step=0.001)
    
with col2 :
     texture_se = st.number_input("Texture SE", min_value=0.360, max_value=4.885, value=1.217, step=0.01)
     area_se = st.number_input("Area SE", min_value=6.802, max_value=542.200, value=40.337, step=0.1)
     compactness_se = st.number_input("Compactness SE", min_value=0.002, max_value=0.135, value=0.025, step=0.001)
     concave_points_se = st.number_input("Concave Points SE", min_value=0.000, max_value=0.053, value=0.012, step=0.001)
     fractal_dimension_se = st.number_input("Fractal Dimension SE", min_value=0.001, max_value=0.030, value=0.004, step=0.001)
    
with st.expander("📉 Worst Feature") :
    
    col1, col2 = st.columns(2)
       
with col1 :    
    radius_worst = st.number_input("Radius Worst", min_value=7.930, max_value=36.040, value=16.269, step=0.01)
    perimeter_worst = st.number_input("Perimeter Worst", min_value=50.410, max_value=251.200, value=107.261, step=0.1)
    smoothness_worst = st.number_input("Smoothness Worst", min_value=0.071, max_value=0.223, value=0.132, step=0.001)
    concavity_worst = st.number_input("Concavity Worst", min_value=0.000, max_value=1.252, value=0.272, step=0.001)
    symmetry_worst = st.number_input("Symmetry Worst", min_value=0.157, max_value=0.664, value=0.290, step=0.001)
    
with col2 :
    texture_worst = st.number_input("Texture Worst", min_value=12.020, max_value=49.540, value=25.677, step=0.01)
    area_worst = st.number_input("Area Worst", min_value=185.200, max_value=4254.000, value=880.583, step=1.0)
    compactness_worst = st.number_input("Compactness Worst", min_value=0.027, max_value=1.058, value=0.254, step=0.001)
    concave_points_worst = st.number_input("Concave Points Worst", min_value=0.000, max_value=0.291, value=0.115, step=0.001)
    fractal_dimension_worst = st.number_input("Fractal Dimension Worst", min_value=0.055, max_value=0.207, value=0.084, step=0.001)
    
col1, col2 = st.columns(2)

with col1:
     predict = st.button("🔍 Predict Cancer", use_container_width=True)

with col2:
       st.button("🔄 Clear (Refresh Page)", use_container_width=True)
       
if predict:
    try:

        with st.spinner("Analyzing patient data..."):
            input_data = [[
            radius_mean,
            texture_mean,
            perimeter_mean,
            area_mean,
            smoothness_mean,
            compactness_mean,
            concavity_mean,
            concave_points_mean,
            symmetry_mean,
            fractal_dimension_mean,
            
            radius_se,
            texture_se,
            perimeter_se,
            area_se,
            smoothness_se,
            compactness_se,
            concavity_se,
            concave_points_se,
            symmetry_se,
            fractal_dimension_se,
            
            radius_worst,
            texture_worst,
            perimeter_worst,
            area_worst,
            smoothness_worst,
            compactness_worst,
            concavity_worst,
            concave_points_worst,
            symmetry_worst,
            fractal_dimension_worst
        
        ]]

            input_data = np.array(input_data)
            input_data = scaler.transform(input_data)

            prediction = model.predict(input_data)
            result = label.inverse_transform(prediction)
            probability = model.predict_proba(input_data)

            st.subheader("📋 Prediction Result")

            if result[0] == "M":
                st.error("⚠️ Malignant (Cancer Detected)")
            else:
                st.success("✅ Benign (No Cancer Detected)")

            st.metric(
                "🟢 Benign Probability",
                f"{probability[0][0]*100:.2f}%"
            )

            st.metric(
                "🔴 Malignant Probability",
                f"{probability[0][1]*100:.2f}%"
            )

    except Exception as e:
        st.error(f"Error: {e}")
           
st.info("🤖 Prediction generated using the K-Nearest Neighbors (KNN) model.")
        
st.divider()
        
st.caption( "Developed by **Bhumit Kalal** | Breast Cancer Prediction using KNN | Streamlit")
        
        
        
        
    
        