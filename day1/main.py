from data import data

#Sol 1
def func(total=2020):
    for initialValue in data:
        for subsequentValue in data:
            if((initialValue != subsequentValue) and (initialValue + subsequentValue == total)):
                return initialValue * subsequentValue

#Sol 2
def func2(total=2020):
    for firstValue in data:
        for secondValue in data:
            for thirdValue in data:
                if((firstValue != secondValue != thirdValue) and (firstValue + secondValue + thirdValue == total)):
                    print(firstValue + secondValue + thirdValue)
                    return firstValue * secondValue * thirdValue


mul = func()
mul2 = func2()

print(mul2)
            