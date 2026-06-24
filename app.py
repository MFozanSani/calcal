import streamlit as st


st.set_page_config(page_title="CalCal", page_icon=":calculator:")
st.title("CalCal - Calculator Calories")


activity_multiplier = {'Sedentary (little/no exercise)':1.2,'Lightly active (1–3 days/week)':1.375,'Moderately active (3–5 days/week)':1.55,'Very active (6–7 days/week)':1.725,'Extremely active (hard exercise + physical job)':1.9}
col1, col2 = st.columns(2)
with col2:
    units = st.radio("Choose units", ["kg/m", "lb/in"])
with col1:
    if units == "kg/m":
        weight_kg = st.number_input("Enter your weight in (kgs)", value=None,width=300, placeholder="Enter your weight")
        height_m = st.number_input("Enter your height in (m)", value=None,width=300, placeholder="Enter your height")
    elif units == "lb/in":
        weight_lb = st.number_input("Enter your weight in (lbs)", value=None,width=300, placeholder="Enter your weight")
        height_in = st.number_input("Enter your height in (in)", value=None,width=300, placeholder="Enter your height")
col3, col4 = st.columns(2)
with col3:
    age = st.number_input("Enter your age", value=None, min_value=0, placeholder="Enter your age")
    sex = st.selectbox("Select your sex/gender", ['Male','Female'], index=None)
with col4:
    activity_level = st.selectbox("Select your activity level", ['Sedentary (little/no exercise)','Lightly active (1–3 days/week)','Moderately active (3–5 days/week)','Very active (6–7 days/week)','Extremely active (hard exercise + physical job)'], index=None)
    goal = st.selectbox("Select your goal", ['Maintain weight','Lose weight', 'Gain weight'], index=None)
if units == "kg/m":
    weight = weight_kg
    height = height_m
if units == "lb/in" and weight_lb is not None and height_in is not None:
    weight = weight_lb /2.205
    height = height_in/39.37
if st.button("Calculate"):
    if weight and height and age and sex and activity_level and goal is not None and weight>0 and height > 0 and age >=0:
        col8, col9 = st.columns(2)
        with col8:
            st.subheader("BMI")
            BMI = round(weight/ (height * height), 2)
            st.write(str(BMI))
            if BMI < 18.5:
                st.write(":red[Underweight]")
            elif BMI >= 18.5 and BMI <= 24.9:
                st.write(":green[Normal]")
            elif BMI >= 25 and BMI <=29.9:
                st.write(":yellow[Overweight]")
            elif BMI >= 30:
                st.write(":red[Obese]")
        with col9:
            st.subheader("BMR - Basal Metabolic Rate")
            if sex == "Male":
                BMR = round((10 * weight) + (6.25 * (height*100)) - (5* age) +5,2)
                st.write(f"Male: {BMR}")
            elif sex == "Female":
                BMR = round((10 * weight) + (6.25 * (height*100)) - (5* age) -161,2)
                st.write(f"Female: {BMR}")
        st.subheader("TDEE (Total Daily Energy Expenditure) — total calories burned per day")
        tdee = round(BMR * activity_multiplier[activity_level], 2)
        st.write(str(tdee))
        st.subheader("Calories Target")
        if goal == "Maintain weight":
            calories = round(tdee, 2)
            st.write(str(calories))
        elif goal == "Lose weight":
            calories = round(tdee - 500, 2)
            st.write(str(calories))
        elif goal == "Gain weight":
            calories = round(tdee +375, 2)
            st.write(str(calories))
        st.subheader("Macronutrient Breakdown")
        col5, col6, col7 = st.columns(3)
        with col5:
            st.write("Protein:")
            if goal == "Maintain weight":
                protein = round(0.8 * weight,2)
                st.write(str(protein))
            elif goal == "Lose weight":
                protein = round(2.1 * weight,2)
                st.write(str(protein))
            elif goal == "Gain weight":
                protein = round(1.9 * weight,2)
                st.write(str(protein))
        with col6:
            fats = round((calories * 0.25)/9,2)
            st.write(f"""
                    Fat:\n 
                    {round(fats,2)},\n 
                    :red[Don't go below ~0.5-0.6g/kg for hormonal health]
                    """)
            remaining_calories = calories-(fats*9)
        with col7:
            st.write("Carbs:")
            if goal == "Maintain weight":
                carbs = round((remaining_calories -(0.8 * weight))/4, 2)
                st.write(str(carbs))
            elif goal == "Lose weight":
                carbs = round((remaining_calories-(2.1 * weight))/4,2)
                st.write(str(carbs))
            elif goal == "Gain weight":
                carbs = round((remaining_calories-(1.9 * weight))/4, 2)
                st.write(str(carbs))
    else:
        st.error("Some fields are empty!")