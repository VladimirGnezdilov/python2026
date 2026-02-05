def is_balanced(string):
        return True
    if len(string) % 2 != 0:
        return False
    pairs = {"(": ")", "[": "]", "{": "}"}
    def find_and_remove_pair(s, start=0):
        if start >= len(s) - 1:
            return None
        if s[start] in pairs and s[start + 1] == pairs[s[start]]:
            return start
        return find_and_remove_pair(s, start + 1)
    pair_start = find_and_remove_pair(string)
    if pair_start is None:
        return False
    new_string = string[:pair_start] + string[pair_start + 2:]
    return is_balanced(new_string)
