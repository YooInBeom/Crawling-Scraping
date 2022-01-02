import matplotlib
import matplotlib.pyplot as plt
import platform

matplotlib.use('Agg')
if platform.system() == 'Darwin':
        plt.rc('font', family='AppleGothic')

plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'bx-', label='첫 번째 함수')
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro--', label='두 번쨰 함수')

plt.xlabel('X 값')
plt.ylabel('Y 값')
plt.title('matplotlib 샘플')
plt.legend(loc='best')
plt.xlim(0, 6)

plt.savefig('graph.png', dpi=300)
