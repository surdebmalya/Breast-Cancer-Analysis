# Created By Debmalya Sur [27-07-2020] [23:59]

import streamlit as st
import joblib
import pandas as pd

st.markdown("<h1 style='text-align: center; color: Green;'><u>Breast Cancer Prediction</u></h1>", unsafe_allow_html=True)

st.text("""""")
st.write("""
## 1️⃣ About
	""")
st.markdown("<hr>", unsafe_allow_html=True)
st.write("""
Hi all, Welcome to this project. It is a Breast Cancer Prediction Project!
	""")
st.write("""
This project is made by **Debmlaya Sur**.
	""")
st.write("""
The model of this project is giving an accuracy of **96.49%**. For more details, please click the button below!
	""")

st.text("""""")
st.write("""
## 2️⃣ How To Use It
	""")
st.markdown("<hr>", unsafe_allow_html=True)
st.write("""
Please Read Carefully The Following Guidelines:
- All The Fields Need To Have A Number As Input
- After Filling Every Input, Press *ENTER* To Save The Data Into The Text Field!
- The Inputs Followed By A ⭕, Is A Required Input
- If There Is No ⭕ In The End, Then You Can Skip That Input
- Every Input Has A Defult Value In It
- After Filling All The Values, Just Click The **👁️‍🗨️ Predict** Button To See What Machine Thinks About The Data!
- Now, Just Go To The Next Section & Start Predicting!
	""")
st.write("""
🔘 **NOTE :** *If Any Required Data Is Missing Then It Will Show An Error As Output!*
	""")

st.text("""""")
st.write("""
## 3️⃣ It's Time To Make Prediction
	""")
st.markdown("<hr>", unsafe_allow_html=True)

st.text("""""")
radious_mean = st.text_input("Radius Mean ⭕", 14.1)
st.text("""""")
texture_mean = st.text_input("Texture Mean ⭕", 19.3)
st.text("""""")
perimeter_mean = st.text_input("Perimeter Mean ", 92)
st.text("""""")
area_mean = st.text_input("Area Mean ", 655)
st.text("""""")
smoothness_mean = st.text_input("Smoothness Mean ⭕", 0.1)
st.text("""""")
compactness_mean = st.text_input("Compactness Mean ", 0.1)
st.text("""""")
concavity_mean = st.text_input("Concavity Mean ", 0.09)
st.text("""""")
concave_points_mean = st.text_input("Concave Points Mean ⭕", 0.05)
st.text("""""")
symmetry_mean = st.text_input("Symmetry Mean ⭕", 0.18)
st.text("""""")
fractal_dimension_mean = st.text_input("Fractal Dimension Mean ⭕", 0.06)

st.text("""""")
radious_se = st.text_input("Radius SE ", 0.41)
st.text("""""")
texture_se = st.text_input("Texture SE ⭕", 1.22)
st.text("""""")
perimeter_se = st.text_input("Perimeter SE ⭕", 2.87)
st.text("""""")
area_se = st.text_input("Area SE ", 40.3)
st.text("""""")
smoothness_se = st.text_input("Smoothness SE ⭕", 0.01)
st.text("""""")
compactness_se = st.text_input("Compactness SE ", 0.03)
st.text("""""")
concavity_se = st.text_input("Concavity SE ⭕", 0.03)
st.text("""""")
concave_points_se = st.text_input("Concave Points SE ", 0.01)
st.text("""""")
symmetry_se = st.text_input("Symmetry SE ⭕", 0.02)
st.text("""""")
fractal_dimension_se = st.text_input("Fractal Dimension SE ⭕", 0)

st.text("""""")
radious_worst = st.text_input("Radius Worst ", 16.3)
st.text("""""")
texture_worst = st.text_input("Texture Worst ", 25.7)
st.text("""""")
perimeter_worst = st.text_input("Perimeter Worst ", 107)
st.text("""""")
area_worst = st.text_input("Area Worst ", 881)
st.text("""""")
smoothness_worst = st.text_input("Smoothness Worst ⭕", 0.13)
st.text("""""")
compactness_worst = st.text_input("Compactness Worst ", 0.25)
st.text("""""")
concavity_worst = st.text_input("Concavity Worst ⭕", 0.27)
st.text("""""")
concave_points_worst = st.text_input("Concave Points Worst ", 0.11)
st.text("""""")
symmetry_worst = st.text_input("Symmetry Worst ⭕", 0.29)
st.text("""""")
fractal_dimension_worst = st.text_input("Fractal Dimension Worst ⭕", 0.08)

def show_output(final_pred):
	st.text("""""")
	st.write("""
	## 🎯 RESULT
		""")
	if final_pred == 'B':
		# benign
		st.text("""""")
		st.write("""
			## 👁️ Model Predicts That The Patient Has A BENIGN Tumor.
			""")
	else:
		# malignant
		st.text("""""")
		st.write("""
			## 👁️ Model Predicts That The Patient Has A MALIGNANT Tumor.
			""")

st.text("""""")
predict = st.button("👁️‍🗨️ Predict")
if predict:
	x_input = []
	try:
		x_input.append(float(radious_mean))
		x_input.append(float(texture_mean))
		x_input.append(float(smoothness_mean))
		x_input.append(float(concave_points_mean))
		x_input.append(float(symmetry_mean))
		x_input.append(float(fractal_dimension_mean))

		x_input.append(float(texture_se))
		x_input.append(float(perimeter_se))
		x_input.append(float(smoothness_se))
		x_input.append(float(concavity_se))
		x_input.append(float(symmetry_se))
		x_input.append(float(fractal_dimension_se))

		x_input.append(float(smoothness_worst))
		x_input.append(float(concavity_worst))
		x_input.append(float(symmetry_worst))
		x_input.append(float(fractal_dimension_worst))

		y = tuple(x_input)
		x_input = [y]
		x_input_df = pd.DataFrame(x_input)

		filename = "finalized_model.sav"
		model = joblib.load(filename)

		prediction = model.predict(x_input_df.iloc[:1,:])
		show_output(prediction[0])

	except:
		st.write("""
					### ❗ Oops!!! Something Went Wrong!!!
				""")
		st.write("""
			### The Model Is Not Working May Be Because:
			- You Might Input Something Other Than A Number 🤔
			- You Might Miss Some Required Inputs 🤔
			""")
		st.write("""
			## Please Try Again!!!
			""")

st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.write("""
### ©️ Created By Debmalya Sur
	""")
