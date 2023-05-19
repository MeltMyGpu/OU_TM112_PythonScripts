'''
Kieran burnett
'''

# Transform a list of tempertures in Fahrenheit to Celcuis and append to new list

def fahrenheit_to_celcuis(input_list: list[int]) -> list[float]:
    output_list = []
    for temperature in input_list:
        result = (temperature - 32) / 1.8
        output_list.append(result)


def celcuis_to_fahrenheit(input_list: list[float]) -> list[float]:
    output_list = []
    for temperature in input_list:
        result = (temperature * 1.8) + 32
        output_list.append(result)
    return output_list

test1 = [-1,0,1]
test1_results = [30.2,32,33.8]

test2 = [-20,-10]
test2_results = [-4,14]

actual1 = celcuis_to_fahrenheit(test1)
actual2 = celcuis_to_fahrenheit(test2)

assert actual1 == test1_results, f'expected {test1_results} got {actual1}'
assert actual2 == test2_results, f'expected {test2_results} got {actual2}'