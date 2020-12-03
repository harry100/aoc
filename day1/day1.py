from data import data

def func(total=2020):
    for initialValue in data:
        for subsequentValue in data:
            if((initialValue != subsequentValue) and (initialValue + subsequentValue == total)):
                return initialValue * subsequentValue

mul = func()
print(mul)
            