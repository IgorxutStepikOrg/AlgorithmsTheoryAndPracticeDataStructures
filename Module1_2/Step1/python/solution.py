bracket_pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
}
open_brackets = bracket_pairs.values()
close_brackets = bracket_pairs.keys()


def check_brackets(string):
    stack = []

    for index, symbol in enumerate(string, start=1):

        if (
            symbol in close_brackets and
            (
                not stack or
                bracket_pairs.get(symbol) != stack.pop().get("symbol")
            )
        ):
            return index

        if symbol in open_brackets:
            stack.append({
                "counter": index,
                "symbol": symbol,
            })

    return stack.pop().get("counter") if stack else "Success"


print(check_brackets(input()))
