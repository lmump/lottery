import random 

def Powerball():
    result = []
    for i in range(5):
        number = random.randint(1,69)
        while (number in result):
            number = random.randint(1,69)
        result.append(number)
    result.sort()
    result.append(random.randint(1,26))
    return result

if __name__ == '__main__':
    result = Powerball()
    print result
