height_cm = "175"
weight_kg = "68.5"

height_cm = int(height_cm)
weight_kg = float(weight_kg)

height_m = height_cm / 100
BMI = weight_kg / (height_m * height_m)
print("BMI:", BMI)