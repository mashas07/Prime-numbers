# TWIN PRIMES
# ----------IMPORT LIBRARIES-------------
import numpy as np
from math import ceil
from scipy import stats
from scipy.integrate import quad
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter

limit = 10000000  # limit under which we look for primes

# opens the list of all primes we are looking for
primes_long = pd.read_csv("/Users/mashasobko/Downloads/numbers.csv")  # need to adjust the pathway

primes_long["value"] = pd.to_numeric(primes_long["value"]).astype(int)  # converts numbers to integers
primes = primes_long[primes_long["value"] < limit]['value'].tolist()  # cuts the list to the required limit


# finds twin primes in list of all primes
def find_twin_primes(primes):
    prime_set = set(primes)
    return [(p, p + 2) for p in primes if (p + 2) in prime_set]


twin_lower = find_twin_primes(primes)  # finds the smallest twin in pair


# finds Gaussian primes (primes ≡ 1 mod 4, plus 2) in list of all primes
def find_gaussian_primes(primes):
    return [p for p in primes if p == 2 or p % 4 == 1]


gaussian_primes = find_gaussian_primes(primes)
"""def calculate_bin_size(twin_lower): #calculates the bin size, so that there are at least 5 primes in a bin
  min_counts_per_bin=5
  sorted_twins = sorted([p for p, _ in twin_lower])
  bin_size=0
  for i in range(len(sorted_twins) - min_counts_per_bin):
    current_gap = sorted_twins[i + min_counts_per_bin] - sorted_twins[i]

    if current_gap > bin_size:
      bin_size= current_gap       
  return ceil(bin_size)




#sorts twin primes in bins
def count_primes_in_bins (twin_lower, num_bins, bin_size): 
    bin_labels = [] #stores the range of each bin
    twin_prime_counts = [] #how many twin primes in the bin


    for i in range(num_bins):
        lo = 2 if i==0 else i * bin_size #lower bin limit
        hi = (i + 1) * bin_size #higher bin limit
        twin_prime_counts.append(sum(1 for p, _ in twin_lower if lo <= p <= hi))
        bin_labels.append(f"{lo}-{hi}")
    observed_values=twin_prime_counts

    return bin_labels, observed_values

#Hardy-Littlewood Conjecture
#sorts expected data in bins
def hardy_littlewood_conjecture(num_bins, bin_size):
  C2=0.6601618158
  expected_values=[]

  def integrand(t): #function inside integral
    return 1/(np.log(t)**2)


  for i in range (num_bins): #calculates the area under the curve for each bin
    lo=2 if i==0 else i*bin_size
    hi=(i+1)* bin_size

    area,_=quad(integrand,lo, hi)
    expected=2*C2*area
    expected_values.append(expected)
  return expected_values

#Goodnes of fit test
def chi_square_goodness_of_fit(observed_values, expected_values):
  statistic=0
  significance_level=0.05 
  for i in range (len(observed_values)): #loops through the prime number values
    statistic=statistic+(np.square(observed_values[i]-expected_values[i])/expected_values[i]) #chi squared statistic formula

  df=len(observed_values)-1
  p_value=stats.chi2.sf(statistic, df) #calculates p_value
  print(f"Chi-square statistic: {statistic:.4f}, p-value: {p_value:.4f}, df: {df}")
  if p_value>significance_level:
    print("Conclusion: Fail to reject H0")
  else:
    print("Conclusion: Reject H0")

#calls the functions
bin_size=calculate_bin_size(twin_lower)
num_bins = ceil(limit/bin_size)
labels, observed_values = count_primes_in_bins(twin_lower, num_bins, bin_size)
for i in range(num_bins): #prints bin label and number of primes in it
    print(f"Bin {labels[i]}: {observed_values[i]} twin primes")

expected_values=hardy_littlewood_conjecture(num_bins, bin_size)

print()
print("H0= there is no significant difference between the distribution of twin primes and Hardy-Littlewood Conjecture ")
print("H1= there is significant difference between the distribution of twin primes and Hardy-Littlewood Conjecture ")
chi_square_goodness_of_fit(observed_values, expected_values) #runs the statistical test"""

# PALINDROMIC PRIMES
import numpy as np  # import library
from math import ceil
from scipy import stats
from scipy.integrate import quad
import pandas as pd
import matplotlib.pyplot as plt

limit = 10000000  # limit under which we look for primes

# opens the list of all primes we are looking for
primes_long = pd.read_csv("/Users/mashasobko/Downloads/numbers.csv")  # need to adjust the pathway
primes_long["value"] = pd.to_numeric(primes_long["value"]).astype(int)  # converts numbers to integers
primes = primes_long[primes_long["value"] < limit]['value'].tolist()  # cuts the list to the required limit


# finds polindromic primes in list of all primes
def find_pol_primes(primes):
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    return [p for p in primes if is_palindrome(p)]


pol_starts = find_pol_primes(primes)  # finds the smallest pol win in pair

"""def calculate_bin_size(pol_starts):
    min_counts_per_bin = 5
    sorted_pol = sorted(pol_starts)          # flat list, no unpacking
    bin_size = 0
    for i in range(len(sorted_pol) - min_counts_per_bin):
        current_gap = sorted_pol[i + min_counts_per_bin] - sorted_pol[i]
        if current_gap > bin_size:
            bin_size = current_gap
    return ceil(bin_size)




#sorts pol primes in bins
def count_primes_in_bins(pol_starts, num_bins, bin_size):
    bin_labels = []
    pol_prime_counts = []
    for i in range(num_bins):
        lo = 2 if i == 0 else i * bin_size
        hi = (i + 1) * bin_size
        pol_prime_counts.append(sum(1 for p in pol_starts if lo <= p <= hi))  # flat list, no unpacking
        bin_labels.append(f"{lo}-{hi}")
    return bin_labels, pol_prime_counts

#Hardy-Littlewood Conjecture
#sorts expected data in bins
def hardy_littlewood_conjecture(num_bins, bin_size):
  C2=0.6601618158
  expected_values=[]

  def integrand(t): #function inside integral
    return 1/(np.log(t)**2)


  for i in range (num_bins): #calculates the area under the curve for each bin
    lo=2 if i==0 else i*bin_size
    hi=(i+1)* bin_size

    area,_=quad(integrand,lo, hi)
    expected=2*C2*area
    expected_values.append(expected)
  return expected_values

#Goodnes of fit test
def chi_square_goodness_of_fit(observed_values, expected_values):
  statistic=0
  significance_level=0.05 
  for i in range (len(observed_values)): #loops through the prime number values
    statistic=statistic+(np.square(observed_values[i]-expected_values[i])/expected_values[i]) #chi squared statistic formula

  df=len(observed_values)-1
  p_value=stats.chi2.sf(statistic, df) #calculates p_value
  print(f"Chi-square statistic: {statistic:.4f}, p-value: {p_value:.4f}, df: {df}")
  if p_value>significance_level:
    print("Fail to reject H0")
  else:
    print("Reject H0")


bin_size=calculate_bin_size(pol_starts)
num_bins = ceil(limit/bin_size)
labels, observed_values = count_primes_in_bins(pol_starts, num_bins, bin_size)
for i in range(num_bins):
    print(f"Bin {labels[i]}: {observed_values[i]} twin primes")

expected_values=hardy_littlewood_conjecture(num_bins, bin_size)

print("H0= there is no significant difference between the distribution of twin primes and Hardy-Littlewood Conjecture ")
print("H1= there is significant difference between the distribution of twin primes and Hardy-Littlewood Conjecture ")
chi_square_goodness_of_fit(observed_values, expected_values)"""

# CIRCULAR PRIMES
import numpy as np
from math import ceil
from scipy import stats
from scipy.integrate import quad
import pandas as pd

limit = 1000000

primes_long = pd.read_csv("/Users/mashasobko/Downloads/numbers.csv")
primes_long["value"] = pd.to_numeric(primes_long["value"]).astype(int)
primes = primes_long[primes_long["value"] < limit]['value'].tolist()

"""def find_circular_primes(primes):
    prime_set = set(primes)
    def is_circular(p):
        s = str(p)
        rotations = [int(s[i:] + s[:i]) for i in range(len(s))]
        return all(r in prime_set for r in rotations)
    return [p for p in primes if is_circular(p)]

def calculate_bin_size(circular_starts):
    min_counts_per_bin = 5
    sorted_circular = sorted(circular_starts)
    bin_size = 0
    for i in range(len(sorted_circular) - min_counts_per_bin):
        current_gap = sorted_circular[i + min_counts_per_bin] - sorted_circular[i]
        if current_gap > bin_size:
            bin_size = current_gap
    return ceil(bin_size)

def count_primes_in_bins(circular_starts, num_bins, bin_size):
    bin_labels = []
    prime_counts = []
    circular_counts = []
    for i in range(num_bins):
        lo = 2 if i == 0 else i * bin_size
        hi = (i + 1) * bin_size
        bin_labels.append(f"{lo}-{hi}")
        prime_counts.append(sum(1 for p in primes if lo <= p <= hi))
        circular_counts.append(sum(1 for p in circular_starts if lo <= p <= hi))
    return bin_labels, prime_counts, circular_counts

def hardy_littlewood_conjecture(num_bins, bin_size):
    C2 = 0.6601618158
    expected_values = []
    def integrand(t):
        return 1 / (np.log(t) ** 2)
    for i in range(num_bins):
        lo = 2 if i == 0 else i * bin_size
        hi = (i + 1) * bin_size
        area, _ = quad(integrand, lo, hi)
        expected_values.append(2 * C2 * area)
    return expected_values

def chi_square_goodness_of_fit(observed_values, expected_values):
    statistic = 0
    significance_level = 0.05
    for i in range(len(observed_values)):
        if expected_values[i] > 0:
            statistic += np.square(observed_values[i] - expected_values[i]) / expected_values[i]
    df = len(observed_values) - 1
    p_value = stats.chi2.sf(statistic, df)
    print(f"Chi-square statistic: {statistic:.4f}, p-value: {p_value:.4f}, df: {df}")
    if p_value > significance_level:
        print("Fail to reject H0")
    else:
        print("Reject H0")

circular_starts = find_circular_primes(primes)
bin_size = calculate_bin_size(circular_starts)
num_bins = ceil(limit / bin_size)
labels, prime_counts, observed_values = count_primes_in_bins(circular_starts, num_bins, bin_size)

for i in range(num_bins):
    print(f"Bin {labels[i]}: {observed_values[i]} circular primes")

expected_values = hardy_littlewood_conjecture(num_bins, bin_size)

print("H0: no significant difference between the distribution of circular primes and the Hardy-Littlewood Conjecture")
print("H1: significant difference exists")
chi_square_goodness_of_fit(observed_values, expected_values)"""

# ----------IMPORT LIBRARIES-------------
import numpy as np  # import library
from math import ceil
from scipy import stats
from scipy.integrate import quad
import pandas as pd
import matplotlib.pyplot as plt

limit = 1000000  # limit under which we look for primes

# opens the list of all primes we are looking for
primes_long = pd.read_csv("/Users/mashasobko/Downloads/numbers.csv")  # need to adjust the pathway

primes_long["value"] = pd.to_numeric(primes_long["value"]).astype(int)  # converts numbers to integers
primes = primes_long[primes_long["value"] < limit]['value'].tolist()  # cuts the list to the required limit


# finds sexy primes in list of all primes
def find_sexy_primes(primes):
    prime_set = set(primes)
    return [(p, p + 6) for p in primes if (p + 6) in prime_set]


sexy_starts = find_sexy_primes(primes)  # finds the smallest sexy in pair

"""def calculate_bin_size(sexy_starts): #calculates the bin size, so that there are at least 5 primes in a bin
  min_counts_per_bin=5
  sorted_sexy = sorted([p for p, _ in sexy_starts])
  bin_size=0
  for i in range(len(sorted_sexy) - min_counts_per_bin):
    current_gap = sorted_sexy[i + min_counts_per_bin] - sorted_sexy[i]

    if current_gap > bin_size:
      bin_size= current_gap       
  return ceil(bin_size)




#sorts sexy primes in bins
def count_primes_in_bins (sexy_starts, num_bins, bin_size): 
    bin_labels = [] #range if each bin
    twin_prime_counts = [] #how many sexy primes in the bin


    for i in range(num_bins):
        lo = 2 if i==0 else i * bin_size #lower bin limit
        hi = (i + 1) * bin_size #higher bin limit
        twin_prime_counts.append(sum(1 for p, _ in sexy_starts if lo <= p <= hi))
        bin_labels.append(f"{lo}-{hi}")
    observed_values=twin_prime_counts

    return bin_labels, observed_values

#Hardy-Littlewood Conjecture
#sorts expected data in bins
def hardy_littlewood_conjecture(num_bins, bin_size):
  C2=1.32032
  expected_values=[]

  def integrand(t): #function inside integral
    return 1/(np.log(t)**2)


  for i in range (num_bins): #calculates the area under the curve for each bin
    lo=2 if i==0 else i*bin_size
    hi=(i+1)* bin_size

    area,_=quad(integrand,lo, hi)
    expected=2*C2*area
    expected_values.append(expected)
  return expected_values

#Goodnes of fit test
def chi_square_goodness_of_fit(observed_values, expected_values):
  statistic=0
  significance_level=0.05 
  for i in range (len(observed_values)): #loops through the prime number values
    statistic=statistic+(np.square(observed_values[i]-expected_values[i])/expected_values[i]) #chi squared statistic formula

  df=len(observed_values)-1
  p_value=stats.chi2.sf(statistic, df) #calculates p_value
  print(f"Chi-square statistic: {statistic:.4f}, p-value: {p_value:.4f}, df: {df}")
  if p_value>significance_level:
    print("Fail to reject H0")
  else:
    print("Reject H0")


bin_size=calculate_bin_size(sexy_starts)
num_bins = ceil(limit/bin_size)
labels, observed_values = count_primes_in_bins(sexy_starts, num_bins, bin_size)
for i in range(num_bins):
    print(f"Bin {labels[i]}: {observed_values[i]} sexy primes")

expected_values=hardy_littlewood_conjecture(num_bins, bin_size)

print("H0= there is no significant difference between the distribution of sexy primes and Hardy-Littlewood Conjecture ")
print("H1= there is significant difference between the distribution of sexy primes and Hardy-Littlewood Conjecture ")
chi_square_goodness_of_fit(observed_values, expected_values)
"""
# Prime Visualization
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def hardy_littlewood_conjecture_twin(x):
    C2_twin = 0.6601618158

    def integrand(t):
        return 1 / (np.log(t) ** 2)

    area, _ = quad(integrand, 2, x)
    return 2 * C2_twin * area


def hardy_littlewood_conjecture_sexy(x):
    C2_sexy = 1.32032

    def integrand(t):
        return 1 / (np.log(t) ** 2)

    area, _ = quad(integrand, 2, x)
    return 2 * C2_sexy * area


xp_circular = [
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199,
    311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793,
    7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193,
    93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919,
    919393, 933199, 939193, 939391, 993319, 999331,
    1111111111111111111, 11111111111111111111111  # R₁₉, R₂₃
]
yp_circular_list = list(range(1, len(xp_circular) + 1))

# Last two repunit primes)
xp_outliers = xp_circular[-2:]
yp_outliers = yp_circular_list[-2:]

limit = max(xp_circular[:54])  # limit for HL curves

x_hl_sexy = np.logspace(np.log10(2), np.log10(limit), 500)
y_hl_sexy = [hardy_littlewood_conjecture_sexy(x) for x in x_hl_sexy]

x_hl_twin = np.logspace(np.log10(2), np.log10(limit), 500)
y_hl_twin = [hardy_littlewood_conjecture_twin(x) for x in x_hl_twin]

xp_sexy = [p for p, _ in sexy_starts]
yp_sexy = list(range(1, len(xp_sexy) + 1))

xp_twin = [p for p, _ in twin_lower]
yp_twin = list(range(1, len(xp_twin) + 1))

xp_pol = pol_starts
yp_pol = list(range(1, len(xp_pol) + 1))

xp_gaussian = gaussian_primes
yp_gaussian = list(range(1, len(xp_gaussian) + 1))


# ── Plot function ─────────────────────────────────────────────────────────────
def plot_all(ax):
    ax.plot(xp_sexy, yp_sexy, marker='.', label='Sexy Primes', color="#608EDD")
    ax.plot(x_hl_sexy, y_hl_sexy, label='H-L Conjecture (Sexy)', color="#2953A1", linewidth=2, alpha=0.7)
    ax.plot(xp_twin, yp_twin, marker='.', label='Twin Primes', color="#A89DDF")
    ax.plot(x_hl_twin, y_hl_twin, label='H-L Conjecture (Twin)', color="#8179A9", linewidth=2)
    ax.plot(xp_pol, yp_pol, marker='.', label='Palindromic Primes', color="#DE7691")
    ax.plot(xp_circular, yp_circular_list, marker='.', label='Circular Primes', color="#C56C51")
    ax.plot(xp_gaussian, yp_gaussian, marker='.', label='Gaussian Primes', color="#79AB73")  # amber


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, dpi=100,
                                    figsize=(14, 6), facecolor="#fff0f5",  # ← change here
                                    gridspec_kw={'width_ratios': [6, 1, 1]})
fig.subplots_adjust(wspace=0.05)

plot_all(ax1)
plot_all(ax2)
plot_all(ax3)

# ── Axis limits ───────────────────────────────────────────────────────────────
ax1.set_xlim(2, 2e6)
ax2.set_xlim(8e17, 2e18)  # R₁₉ = 1111111111111111111 ≈ 1.11e18
ax3.set_xlim(8e21, 2e23)  # R₂₃ = 11111111111111111111111 ≈ 1.11e22

# ── Scales, ticks, background ─────────────────────────────────────────────────
for ax in (ax1, ax2, ax3):
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_ylim(bottom=1, top=18000)
    ax.set_facecolor("#fff5fb")
    ax.tick_params(colors="#202940", axis='y', which='both', left=False)
    ax.tick_params(colors="#202940", axis='x', which='both', bottom=False)

    ax.grid(True, which='major', linestyle=':', linewidth=0.8, color='#b0b0b0', alpha=0.6)
    ax.set_axisbelow(True)

    ax.xaxis.get_offset_text().set_visible(False)
    from matplotlib.ticker import NullFormatter

    ax.xaxis.set_minor_formatter(NullFormatter())

ax1.set_xticks([1e1, 1e2, 1e3, 1e4, 1e5, 1e6])
ax1.set_xticklabels(['$10^1$', '$10^2$', '$10^3$', '$10^4$', '$10^5$', '$10^6$'])

ax2.set_xticks([1e18])
ax2.set_xticklabels(['$10^{18}$'])

ax3.set_xticks([1e22])
ax3.set_xticklabels(['$10^{22}$'])

# ── Broken-axis spines ────────────────────────────────────────────────────────
ax1.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax2.tick_params(left=False)
ax3.tick_params(left=False)

# ── Diagonal break markers ────────────────────────────────────────────────────
d = 0.85
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=15,
              linestyle='none', color='#202940', mec='#202940', mew=1, clip_on=False)

ax1.plot([1, 1], [0, 1], transform=ax1.transAxes, **kwargs)  # right edge ax1
ax2.plot([0, 0], [0, 1], transform=ax2.transAxes, **kwargs)  # left  edge ax2
ax2.plot([1, 1], [0, 1], transform=ax2.transAxes, **kwargs)  # right edge ax2
ax3.plot([0, 0], [0, 1], transform=ax3.transAxes, **kwargs)  # left  edge ax3

# ── Labels, title, legend ─────────────────────────────────────────────────────
fig.suptitle('Distribution of Prime Types vs. Hardy-Littlewood Conjecture\n(log–log scale)',
             fontsize=14, color="#c71585")
ax1.set_xlabel('Natural Number', fontsize=14, color="#c71585")
ax2.set_xlabel('', fontsize=11)
ax3.set_xlabel('', fontsize=11)

ax1.set_ylabel('Number of Prime Numbers', fontsize=14, color="#c71585")
ax1.legend(loc='upper left', fontsize=12)

plt.show()