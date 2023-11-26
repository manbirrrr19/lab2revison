import Exercise2

def test_find_min_max():
    result = []
    input_arr = [5, 67, 32] #put this list inside the func from Exercise 2
    test = (5, 67) #manually calc

    result = Exercise2.find_min_max(input_arr)

    assert (result == test)



def test_calc_average():
    result = []
    input_arr = [5, 67, 32]
    test = 34.666666666666664 #manual calc

    result = Exercise2.calc_average(input_arr)

    assert (result == test)


def test_calc_median_temperature():
    result = []
    input_arr = [5, 67, 32]
    test = 32

    result = Exercise2.calc_median_temperature(input_arr)

    assert (result == test)