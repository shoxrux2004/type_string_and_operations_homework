def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    z=(x+y)*2
    return f"({x}+{y})*2={z}"
print(main(3,7))