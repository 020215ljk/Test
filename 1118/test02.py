import numpy as np

# Sigmoid激活函数及其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 输入数据
X = np.array([[0.4, 0.7]])

# 目标输出
y = np.array([[1]])

# 随机初始化权重和偏置
np.random.seed(1)
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

weights_input_hidden = np.random.rand(input_neurons, hidden_neurons)
bias_hidden = np.random.rand(1, hidden_neurons)
weights_hidden_output = np.random.rand(hidden_neurons, output_neurons)
bias_output = np.random.rand(1, output_neurons)

# 设置学习率和迭代次数
learning_rate = 0.1
epochs = 10000

# 训练模型
for epoch in range(epochs):
    # 前向传播
    hidden_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_output = sigmoid(hidden_input)

    output_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    output = sigmoid(output_input)

    # 计算损失
    loss = np.mean(np.square(y - output))

    # 反向传播
    output_error = y - output
    output_delta = output_error * sigmoid_derivative(output)

    hidden_error = output_delta.dot(weights_hidden_output.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)

    # 梯度的向量化计算和参数更新
    output_grad = np.dot(hidden_output.T, output_delta)
    hidden_grad = np.dot(X.T, hidden_delta)

    weights_hidden_output += output_grad * learning_rate
    bias_output += np.sum(output_delta) * learning_rate

    weights_input_hidden += hidden_grad * learning_rate
    bias_hidden += np.sum(hidden_delta) * learning_rate

    if epoch % 1000 == 0:
        print(f'Epoch: {epoch}, Loss: {loss}')

print("\nOutput after training:")
print(output)
