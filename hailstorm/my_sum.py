def my_sum(*args):
    result = 0
    for number in args:
        result += number

    print(f'The sum of {args} = {result}')
    return result

my_sum(10, 20, 30, 40)
