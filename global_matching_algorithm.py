# -*- encoding: utf-8 -*-
'''
@file: Global algorithm for matching clusters.py
@Author: Xuanlong
@email: qxlpku@gmail.com
''' 
def global_chi_square_matching(chi_square_matrix):
    import heapq

    num_rows = len(chi_square_matrix)
    num_cols = len(chi_square_matrix[0]) if num_rows > 0 else 0
    
    # Step 1: Create a list of all chi statistics with their indices
    chi_values = []
    for i in range(num_rows):
        for j in range(num_cols):
            chi_values.append((chi_square_matrix[i][j], i + 1, j + 1))  # Store values with 1-based indices

    # Sort in descending order based on chi values
    chi_values.sort(reverse=True, key=lambda x: x[0])

    matched_pairs = []
    used_rows = set()
    used_cols = set()

    # Function to check if the current chi value can be kept
    def can_keep(value, row, col):
        return (value == max(chi_square_matrix[row - 1])) and (value == max(chi_square_matrix[r][col - 1] for r in range(num_rows)))

    # Step 2: Attempt to match clusters
    for value, row, col in chi_values:
        if len(matched_pairs) >= 6:
            break
        if row not in used_rows and col not in used_cols and can_keep(value, row, col):
            matched_pairs.append((row, col))
            used_rows.add(row)
            used_cols.add(col)

            # Step 3: Drop all other chi statistics in the corresponding row and column
            for r in range(num_rows):
                chi_square_matrix[r][col - 1] = float('-inf')
            for c in range(num_cols):
                chi_square_matrix[row - 1][c] = float('-inf')

    # Step 4: Repeat until we have 6 matches or exhaust options
    while len(matched_pairs) < 6:
        # Look for the next best option
        for value, row, col in chi_values:
            if row not in used_rows and col not in used_cols and can_keep(value, row, col):
                matched_pairs.append((row, col))
                used_rows.add(row)
                used_cols.add(col)
                
                # Drop other chi statistics
                for r in range(num_rows):
                    chi_square_matrix[r][col - 1] = float('-inf')
                for c in range(num_cols):
                    chi_square_matrix[row - 1][c] = float('-inf')
                break
        else:
            break  # No more matches possible

    # Check if we successfully matched all clusters
    if len(matched_pairs) == 6:
        print("Matching complete")
        print("Matched indices (1-based):", matched_pairs)
        return matched_pairs
    else:
        print("Matching failed")
        return []

# Example usage
chi_square_matrix = [
    [-0.61, 0.12, 0.61, -0.43, -0.39, 0.35],
    [0.64, -0.15, -0.28, -0.20, -0.48, 1.27],
    [0.17, 0.11, -0.12, -0.27, 0.28, -0.70],
    [-0.31, -0.01, -0.39, 0.85, 0.09, -0.28],
    [0.20, 0.17, -0.12, -0.42, -0.24, 0.45],
    [-0.39, -0.57, 0.33, 0.59, 0.42, -0.72]
]

result = global_chi_square_matching(chi_square_matrix)