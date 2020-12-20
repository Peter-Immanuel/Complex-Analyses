from math import sqrt, atan, degrees


class ComplexAnalyses:
    ''' A function to perform basic complex operation and conversion'''
    def __init__(self,*numbers):
        self.numbers = [complex(number) for number in numbers]
        self.__results = {}

    def add(self):
        result = 0
        for number in self.numbers:
            result += number
        self.__results['result'] = result
        return (result, self.__results['Add result'])

    def sub(self):
        numbers = self.numbers
        result = numbers.pop(0)
        for number in numbers:
            result = result - number
        self.__results['result'] = result
        return result

    def mul(self):
        numbers = self.numbers
        result = numbers.pop(0)
        for number in numbers:
            result = result * number
            # print(result)
        self.__results['result'] = result
        return (result, self.__results['result'])

    def div(self):
        numbers = self.numbers
        result = numbers.pop(0)
        for number in numbers:
            result = result / number
        self.__results['result'] = result
        return result

    def convert(self ):
        result = self.__results['result']
        mod = sqrt((result.real**2) + (result.imag ** 2))
        exponential_arg = atan(result.imag/result.real)
        polar_arg = degrees(atan(result.imag/result.real))

        self.__results['modulus'] = mod
        self.__results['Polar Argument'] = polar_arg
        self.__results['exponential Argument'] = exponential_arg

    def get_form(self, form):
        self.convert()
        form.lower()
        if form == 'p':
            return (self.__results['modulus'], self.__results['Polar Argument'])
        elif form == 'e':
            return (self.__results['modulus'], self.__results['exponential Argument'])

