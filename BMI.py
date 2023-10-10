# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）
# 帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

weight = input("请输入您的体重：")
height = input("请输入您的身高：")

BMI = float(weight) / ((float(height)) * (float(height)))
# BMI = float(weight) / ((float(height))^2)
# BMI = weight / (height * height)

if BMI < 18.5:
    print("您的体重过低！")
elif (BMI < 25) and (BMI >= 18.5):
    print("您的体重正常！")
elif (BMI < 28) and (BMI >= 25):
    print("您的体重过重！")
elif (BMI < 32) and (BMI >= 28):
    print("您的体重肥胖！")
else:
    print("您的体重严重肥胖！！！")
