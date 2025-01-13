# using Binet's formula: 
#               F(n) = (1 / sqrt(5)) * (PHI^n - (-PHI)^(-n))
# also where    -1 / PHI = 1 - PHI

# Assuming                  (-PHI)^(-n) tends to 0 for large n
# Hence we solve to get     n >= log(1e999 * sqrt(5)) / log(PHI)

import math

PHI = (1 + math.sqrt(5)) / 2

def solve():
	limit = (999 + math.log10(math.sqrt(5))) / math.log10(PHI)
	return math.ceil(limit)


if __name__ == "__main__":
	print(solve())