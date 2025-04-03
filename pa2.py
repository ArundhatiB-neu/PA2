import sys
import time

def construct_target(target, wordbank, memo):
    if target in memo:
        return memo[target]

    print("Solving for:", target)

    if target == "":
        return [[]]

    result = []

    for word in wordbank:
        if target.startswith(word):
            new_target = target[len(word):]
            new_ways = construct_target(new_target, wordbank, memo)

            for way in new_ways:
                new_way = [word] + way
                result.append(new_way)

    memo[target] = result
    return result


def main():
    if "--target" not in sys.argv or "--wordbank" not in sys.argv:
        print("Usage: python program.py --target <string> --wordbank <words>")
        return

    target_index = sys.argv.index("--target") + 1
    wordbank_index = sys.argv.index("--wordbank") + 1

    try:
        target = sys.argv[target_index]
        wordbank = sys.argv[wordbank_index:]
    except IndexError:
        print("Error: Invalid input format.")
        return

    start_time = time.time()

    result = construct_target(target, wordbank, memo={})

    end_time = time.time()
    runtime = end_time - start_time

    print(f"\nNumber of ways: {len(result)}")
    print("[")

    for way in result:
        print("  ", way)

    print("]")
    print(f"Runtime: {runtime:.6f} seconds")


if __name__ == "__main__":
    main()
