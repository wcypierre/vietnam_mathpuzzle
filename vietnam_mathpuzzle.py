from __future__ import division

# Faster solution for http://gizmodo.com/can-you-solve-this-vietnamese-math-puzzle-for-8-year-ol-1705734738?utm_campaign=socialflow_gizmodo_facebook&utm_source=gizmodo_facebook&utm_medium=socialflow

for v1 in range(1, 10):
	for v2 in range(1, 10):
		if v2 == v1: 
			continue
		else:
			for v3 in range(1, 10):
				if v3 == v1 or v3 == v2: 
					continue
				else:
					for v4 in range(1, 10):
						if v4 == v1 or v4 == v2 or v4 == v3: 
							continue
						else:
							for v5 in range(1, 10):
								if v5 == v1 or v5 == v2 or v5 == v3 or v5 == v4:
									continue
								else:
									for v6 in range(1, 10):
										if v6 == v1 or v6 == v2 or v6 == v3 or v6 == v4 or v6 == v5:
											continue
										else:
											for v7 in range(1, 10):
												if v7 == v1 or v7 == v2 or v7 == v3 or v7 == v4 or v7 == v5 or v7 == v6:
													continue
												else:
													for v8 in range(1, 10):
														if v8 == v1 or v8 == v2 or v8 == v3 or v8 == v4 or v8 == v5 or v8 == v6 or v8 == v7:
															continue
														else:
															for v9 in range(1, 10):
																if v9 == v1 or v9 == v2 or v9 == v3 or v9 == v4 or v9 == v5 or v9 == v6 or v9 == v7 or v9 == v8:
																	continue
																else:
																	if v1 + (13 * (v2 / v3)) + v4 + (12 * v5) - v6 - 11 + ((v7 * v8) / v9) - 10 == 66.0:
																		print "%s + (13 x (%s / %s)) + %s + (12 x %s) - %s - 11 + ((%s x %s) / %s) - 10" % (v1, v2, v3, v4, v5, v6, v7, v8, v9)