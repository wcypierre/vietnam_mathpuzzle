from __future__ import division
import itertools

# Slow solution for http://gizmodo.com/can-you-solve-this-vietnamese-math-puzzle-for-8-year-ol-1705734738?utm_campaign=socialflow_gizmodo_facebook&utm_source=gizmodo_facebook&utm_medium=socialflow

for v1,v2,v3,v4,v5,v6,v7,v8,v9 in itertools.product([1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=9):
	if (v1 == v2 or v1 == v3 or v1 == v4 or v1 == v5 or v1 == v6 or v1 == v7 or v1 == v8 or v1 == v9) or (v2 == v1 or v2 == v3 or v2 == v4 or v2 == v5 or v2 == v6 or v2 == v7 or v2 == v8 or v2 == v9) or (v3 == v1 or v3 == v2 or v3 == v4 or v3 == v5 or v3 == v6 or v3 == v7 or v3 == v8 or v3 == v9) or (v4 == v1 or v4 == v2 or v4 == v3 or v4 == v5 or v4 == v6 or v4 == v7 or v4 == v8 or v4 == v9) or (v5 == v1 or v5 == v2 or v5 == v3 or v5 == v4 or v5 == v6 or v5 == v7 or v5 == v8 or v5 == v9) or (v6 == v1 or v6 == v2 or v6 == v3 or v6 == v4 or v6 == v5 or v6 == v7 or v6 == v8 or v6 == v9) or (v7 == v1 or v7 == v2 or v7 == v3 or v7 == v4 or v7 == v5 or v7 == v6 or v7 == v8 or v7 == v9) or(v8 == v1 or v8 == v2 or v8 == v3 or v8 == v4 or v8 == v5 or v8 == v6 or v8 == v7 or v8 == v9) or (v9 == v1 or v9 == v2 or v9 == v3 or v9 == v4 or v9 == v5 or v9 == v6 or v9 == v7 or v9 == v8):
		continue
	else:
		result = v1 + (13 * (v2 / v3)) + v4 + (12 * v5) - v6 - 11 + ((v7 * v8) / v9) - 10
		if result == 66.0:
			print 1