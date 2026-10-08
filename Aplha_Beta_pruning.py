def alpha_beta(depth, node, maximizing, values, alpha, beta, height):
    # Leaf node
    if depth == height:
        return values[node]

    if maximizing:
        best = float('-inf')

        for child in [node * 2, node * 2 + 1]:
            value = alpha_beta(
                depth + 1, child, False,
                values, alpha, beta, height
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Beta cut-off
            if alpha >= beta:
                break

        return best

    else:
        best = float('inf')

        for child in [node * 2, node * 2 + 1]:
            value = alpha_beta(
                depth + 1, child, True,
                values, alpha, beta, height
            )

            best = min(best, value)
            beta = min(beta, best)

            # Alpha cut-off
            if alpha >= beta:
                break

        return best


# Leaf node values
values = [3, 5, 2, 9, 12, 5, 23, 23]

height = 3

alpha = float('-inf')
beta = float('inf')

result = alpha_beta(
    0, 0, True,
    values, alpha, beta, height
)

print("The optimal value is:", result)