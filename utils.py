from pprint import pprint


def compare(s1, s2):
    s1, s2 = [s.lower() for s in [s1, s2]]
    ngrams = [s1[i:i + 3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max(len(s1), len(s2))

def remove_symbols(s):
    symbols_to_remove = ",!?."
    for symbol in symbols_to_remove:
        s = s.replace(symbol, "")
    return s

def int_val(s):
    try:
        return int(s)
    except ValueError:
        return 0


if __name__ == '__main__':
    out = []
    for a, b in [
        ('алгоритм', 'алгоритм'),
        ('алгоритм', 'алгоритмы'),
        ('алгоритм', 'алгоритмов'),
        ('стол', 'столик'),
        ('стол', 'стул'),
        ('маша', 'даша'),
        ('ольга', 'олег'),
        ('Ольга', 'Наташа'),
        ('маша', 'машенька'), ]:
        out += [(a, b, compare(a, b))]
        pprint(out)
        pprint([int_val(s) for s in ['старше', '30', 'но', '101']])