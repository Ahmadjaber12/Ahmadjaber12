import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# Define the function
def f(t):
    return 53 / (1 + t**2) - 2 * np.exp(-0.5 * t) - 3

# Find exact root
root = brentq(f, 3, 5)

# t values over valid interval [3, 5]
t = np.linspace(2.5, 5.5, 600)
y = f(t)

# False Position iterates
fp_t = [4.24437, 3.99996, 3.92374, 3.89998, 3.89246,
        3.88993, 3.88907, 3.88881, 3.88873]
fp_f = [f(x) for x in fp_t]

# Plot
fig, ax = plt.subplots(figsize=(11, 6.5))

# Function curve
ax.plot(t, y, color='royalblue', linewidth=2.5,
        label=r'$f(t) = \frac{53}{1+t^2} - 2e^{-0.5t} - 3$')

# Zero line
ax.axhline(0, color='black', linewidth=1.0, linestyle='--', label='f(t) = 0')

# Shade valid interval
ax.axvspan(3, 5, alpha=0.08, color='green', label='Valid interval [3, 5]')

# Boundary points
ax.plot(3, f(3), 's', color='green',  markersize=10,
        label=f'$t_L = 3$,  f = {f(3):.4f}')
ax.plot(5, f(5), 's', color='orange', markersize=10,
        label=f'$t_U = 5$,  f = {f(5):.4f}')

# False Position iterates
ax.scatter(fp_t, fp_f, color='gray', s=45, zorder=4, label='FP iterates $t_r$')
for i, (tx, fy) in enumerate(zip(fp_t, fp_f)):
    ax.annotate(f' {i+1}', (tx, fy), fontsize=8, color='dimgray')

# Root marker
ax.plot(root, 0, '*', color='red', markersize=18, zorder=5,
        label=f'Root  $t \\approx {root:.5f}$')
ax.annotate(f'  Root\n  t ≈ {root:.4f}',
            xy=(root, 0), xytext=(root + 0.15, 0.35),
            fontsize=10, color='red', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

# Vertical dashed line at root
ax.axvline(root, color='red', linewidth=1.2, linestyle=':', alpha=0.6)

# Labels, title, legend, grid
ax.set_xlabel('Time  t', fontsize=13)
ax.set_ylabel('f(t)', fontsize=13)
ax.set_title('False Position Method\n'
             r'$f(t)=\frac{53}{1+t^2}-2e^{-0.5t}-3=0$'
             f'   |   Root ≈ {root:.4f}',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=9, loc='upper right')
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_ylim(-2, 4)

plt.tight_layout()
plt.savefig('false_position_plot.png', dpi=150, bbox_inches='tight')
print(f"Plot saved. Root = {root:.6f}")
