''' 
Kieran burnett / KB22678

I'm doing it inside a fucntion cause it looks much nicer
'''

# generate a list by filtering an input list
# Returns a list containing only values greater than teh filter value
def hot_days(input_list: list[int] , filter_value: int) -> list[int]:
    output_temps = []
    for temp in input_list:
        if temp > filter_value:
            output_temps.append(temp)
    return output_temps


test_list = [20,22,10,21,19,20.1,24,29,12,8,-1,0.1]
test_filter = 20

result = hot_days(test_list,test_filter)
print(result)
