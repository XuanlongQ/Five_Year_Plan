import numpy as np
import pandas as pd
from scipy.stats import pearsonr

x1 = np.array([-0.19,-0.30,0.30,0.11,-0.03,0.00,-0.07,0.15,-0.12,-0.18,0.42,-0.04,-0.10,0.14,-0.02,0.17,-0.15,-0.08,0.06,0.07,0.03,-0.09,0.23,-0.10,-0.02,-0.08,0.02])
y3 = np.array([-0.03,-0.06,0.06,-0.38,-0.32,-0.25,0.36,-0.12,-0.19,0.15,0.00,-0.24,-0.18,-0.11,-0.13,0.20,-0.26,-0.14,0.28,0.11,-0.25,-0.16,0.19,-0.03,-0.44,-0.35,-0.35])

x2 = np.array([-0.03,-0.13,0.13,0.04,-0.01,0.19,-0.27,-0.03,0.29,-0.30,0.33,0.20,0.10,0.33,0.08,0.26,0.28,-0.03,0.08,0.27,0.06,0.12,0.05,0.35,0.14,0.24,0.33])
y6 = np.array([0.67,-0.57,0.57,1.35,0.28,0.85,-1.15,-0.32,1.47,-1.56,1.11,1.55,0.53,0.56,0.42,0.69,1.52,0.92,-0.62,0.08,0.97,0.57,0.48,0.74,1.32,2.01,2.03])

x3 = np.array([0.20,0.26,-0.26,0.04,0.11,0.10,0.04,0.07,-0.12,0.09,-0.13,-0.04,0.03,0.18,0.06,-0.14,-0.10,-0.06,-0.05,0.03,-0.06,0.17,-0.13,0.02,-0.09,-0.17,-0.13])
y5 = np.array([-0.02,-0.34,0.34,0.01,-0.13,-0.29,0.23,-0.09,-0.10,0.15,-0.10,-0.16,0.23,-0.33,-0.30,-0.27,-0.29,-0.08,-0.22,-0.15,-0.16,-0.32,-0.19,-0.07,-0.35,-0.19,-0.22])

x4 = np.array([-0.41,0.05,-0.05,-0.17,-0.16,-0.36,0.23,-0.25,0.08,0.34,-0.25,-0.33,-0.06,-0.41,-0.07,-0.06,-0.22,-0.11,0.08,0.10,-0.34,-0.32,-0.16,-0.11,-0.13,-0.10,-0.16])
y4 = np.array([-0.58,0.32,-0.32,-0.97,-0.64,-0.48,0.86,-0.48,-0.23,0.62,-0.49,-0.57,-0.54,-0.63,-0.42,-0.12,-0.24,-0.16,0.77,0.46,-0.37,-0.42,-0.28,-0.37,-0.23,-0.31,-0.30])

x5 = np.array([0.21,-0.15,0.15,0.19,0.08,0.20,-0.18,0.19,-0.07,-0.14,0.00,0.21,0.03,0.03,0.15,-0.03,0.35,0.31,-0.23,-0.28,0.34,0.19,0.17,-0.04,0.29,0.33,0.22])
y1 = np.array([0.08,-0.05,0.05,0.34,0.01,0.77,-0.49,0.24,0.16,-0.75,0.52,0.75,0.53,0.00,0.34,0.13,0.08,-0.06,-0.58,-0.50,0.14,0.42,0.00,-0.02,0.08,-0.09,0.00])

x6 = np.array([0.04,0.10,-0.10,-0.31,-0.09,-0.23,0.23,-0.22,0.06,0.09,-0.22,0.03,-0.02,-0.36,-0.28,-0.05,-0.15,-0.07,0.16,-0.15,-0.04,-0.24,-0.09,-0.10,-0.18,-0.18,-0.21])
y2 = np.array([0.06,0.40,-0.40,0.17,0.62,0.00,-0.28,0.43,-0.26,0.39,-0.35,-0.33,-0.21,0.47,0.21,-0.21,-0.01,-0.04,0.05,0.01,0.11,0.20,-0.04,0.02,0.27,-0.08,-0.11])



xs = [x1, x2, x3, x4, x5, x6]
ys = [y1, y2, y3, y4, y5, y6]

for i, x in enumerate(xs):
    for j, y in enumerate(ys):
        if len(x) > 1 and len(y) > 1: 
            corr, _ = pearsonr(x, y)
            print(f'Pearson correlation between x{i+1} and y{j+1}: {corr:.2f}')