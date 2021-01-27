def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
        return '' #str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


 def recursive_reverse_mem(number):
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))


def revesre_slice(nums):
    return str(nums)[::-1]

print('Функция с использованием срезов revesre_slice')
print(
    timeit(
        'revesre_slice(num_100)',
        setup='from __main__ import revesre_slice, num_100',
        number=10000))
print(
    timeit(
        'revesre_slice(num_1000)',
        setup='from __main__ import revesre_slice, num_1000',
        number=10000))
print(
    timeit(
        'revesre_slice(num_10000)',
        setup='from __main__ import revesre_slice, num_10000',
        number=10000))


def reverse_with_for(nums):
    reversed_str = ''
    for el in str(nums):
        reversed_str = el + reversed_str
    return reversed_str

print('Функция с использованием цикла for')
print(
    timeit(
        'reverse_with_for(num_100)',
        setup='from __main__ import reverse_with_for, num_100',
        number=10000))
print(
    timeit(
        'reverse_with_for(num_1000)',
        setup='from __main__ import reverse_with_for, num_1000',
        number=10000))
print(
    timeit(
        'reverse_with_for(num_10000)',
        setup='from __main__ import reverse_with_for, num_10000',
        number=10000))

"""
    В качестве альтернатив приведенным алгоритмам я использовал срезы и цикл for.
    Замеры однозначно показали, что алгоритм с мемоизацией обладает наименьшим временем
    исполнения несмотря на рекурсию (хотя от срезов я ожидал большего).
    Для срезов мы имеем константную сложность O(1),
    а для цикла for - сложность линейная O(n).
"""