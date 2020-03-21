

class Function():

    '''klasa zawierajaca dwie metody obliczania przyblizen wielomianu'''

    def __init__(self, interval, coefficients):
        self.interval = interval
        self.coeffs = coefficients

    def f(self, x, coefs=[]):
        lista_do_funkcji = []
        for i in coefs:
            lista_do_funkcji.append(i * x ** int(abs(coefs.index(i) - (len(coefs) - 1))))
        return sum(lista_do_funkcji)

    def derivative(self, coefs=[]):
        values = []
        for i in coefs:
            exponent = int(abs(coefs.index(i) - (len(coefs) - 1)))
            if exponent != 0:
                values.append(i * exponent)
        return values

    def check_if_ok(self, interval=[]):
        if self.f(interval[0]) * self.f(interval[1]) < 0:
            return 1
        else:
            return "Not valid youre an idiot"

    def newtons_method_formula(self):
        for number in self.interval:
            if self.f(number, self.coeffs) * self.f(number, self.derivative(self.coeffs)) > 0:
                iteration = number - (self.f(number, self.coeffs) / self.f(number, self.derivative(self.coeffs)))
                return iteration

    def newtons_method(self, number_of_iterations):
        print("\n\n*newtons_method*\n")
        c = 1
        while c != number_of_iterations + 1:
            x = self.newtons_method_formula()
            print("x" + str(c) + " = " + str(self.newtons_method_formula()))
            if self.check_if_ok([self.interval[0], x]) == 1:
                self.interval = [self.interval[0], x]
            else:
                self.interval = [x, self.interval[1]]
            c = c + 1
        return "\n --- dziekuje za skorzystanie z metody stycznych ---\n\n"

    def bisection_method(self, number_of_iterations):
        print("\n\n*bisection_method*\n")
        c = 0
        while c != number_of_iterations + 1:
            x = (self.interval[0] + self.interval[1]) / 2
            print("x" + str(c) + " = " + str(x))
            if self.check_if_ok([self.interval[0], x]) == 1:
                self.interval = [self.interval[0], x]
            else:
                self.interval = [x, self.interval[1]]
            c = c + 1
        return "\n --- dziekuje za skorzystanie z metody bisekcji ---\n\n"
