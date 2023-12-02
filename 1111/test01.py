def f(x):
    return x ** 2


def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


# 计算在 x=2 处的导数
x_value = 2
derivative_forward = forward_difference(f, x_value)
derivative_central = central_difference(f, x_value)

print(f"导数 (前向差分): {derivative_forward}")
print(f"导数 (中心差分): {derivative_central}")
