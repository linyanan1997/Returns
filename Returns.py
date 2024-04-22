import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取股票数据
df = pd.read_csv('stock_data.csv')

# 计算每日收益率
df['Returns'] = df['Close'].pct_change()

# 绘制收益曲线
plt.figure(figsize=(10, 6))
plt.plot(df['Returns'], label='Returns')
plt.legend()
plt.title('Stock Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.show()

# 计算基本统计指标
mean_return = df['Returns'].mean()
std_return = df['Returns'].std()
max_return = df['Returns'].max()
min_return = df['Returns'].min()

print('Mean Return:', mean_return)
print('Standard Deviation of Return:', std_return)
print('Maximum Return:', max_return)
print('Minimum Return:', min_return)
