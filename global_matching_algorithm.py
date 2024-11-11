def global_chi_square_matching(chi_square_matrix):
    import heapq

    # Flatten the matrix and store values with their indices
    sorted_statistics = []
    for i, row in enumerate(chi_square_matrix):
        for j, value in enumerate(row):
            heapq.heappush(sorted_statistics, (-value, i + 1, j + 1))  # Use negative for max heap

    matched_indices = []
    used_rows = set()
    used_cols = set()

    # Attempt to match clusters
    while sorted_statistics and len(matched_indices) < 6:
        value, row, col = heapq.heappop(sorted_statistics)
        if row not in used_rows and col not in used_cols:
            matched_indices.append((row, col))
            used_rows.add(row)
            used_cols.add(col)

    # Check if all clusters are matched
    if len(matched_indices) == 6:
        print("Matching complete")
        print("Matched indices (1-based):", matched_indices)
        return matched_indices
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