from collections import deque

def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque()

    # Initial state: both jugs are empty
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Target reached
        if jug1 == target or jug2 == target:
            print("Solution:")
            for step in path:
                print(step)
            print(f"Final State: ({jug1}, {jug2})")
            return

        states = [
            (capacity1, jug2, "Fill Jug 1"),
            (jug1, capacity2, "Fill Jug 2"),
            (0, jug2, "Empty Jug 1"),
            (jug1, 0, "Empty Jug 2"),
            
            # Pour Jug 1 -> Jug 2
            (
                jug1 - min(jug1, capacity2 - jug2),
                jug2 + min(jug1, capacity2 - jug2),
                "Pour Jug 1 -> Jug 2"
            ),

            # Pour Jug 2 -> Jug 1
            (
                jug1 + min(jug2, capacity1 - jug1),
                jug2 - min(jug2, capacity1 - jug1),
                "Pour Jug 2 -> Jug 1"
            )
        ]

        for new_jug1, new_jug2, action in states:
            if (new_jug1, new_jug2) not in visited:
                queue.append(
                    (new_jug1, new_jug2, path + [action])
                )


# 4-liter and 3-liter jugs
# Target = 2 liters
water_jug(4, 3, 2)