def most_frequent(data: list) -> str:
    return max(set(data), key=data.count)
