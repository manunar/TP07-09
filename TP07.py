class Fraction:
    """Class representing a fraction and operations on it"""

    def __init__(self, num: int = 0, den: int = 1):
        """
        This builds a fraction based on some numerator and denominator.
        PRE : None (type is verified before setting attributes)
        POST : self.numerator and self.denominator are stored as the most reduced form.
        RAISES : ValueError if den = 0
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        self._num = num
        self._den = den
        self.reduce_form()

    @property
    def numerator(self):
        """Return the numerator of the fraction."""
        return self._num

    @property
    def denominator(self):
        """Return the denominator of the fraction."""
        return self._den

    def gcd(self, n: int, d: int):
        """
        Compute the GCD using Euclid's algorithm.
        PRE : n and d are integers
        POST : Returns the greatest common divisor (GCD) of n and d
        RAISES : TypeError if either n or d is not an int
        """
        if not (isinstance(n, int) and isinstance(d, int)):
            raise TypeError("Both parameters of the gcd() method need to be of type int")
        while d != 0:
            n, d = d, n % d
        return abs(n)

    def reduce_form(self):
        """
        Reduce the fraction to its simplest form by dividing both the numerator and the denominator by their GCD.
        PRE : The fraction is initialized
        POST : The fraction is in the most reduced form
        RAISES : None
        """
        d = self.gcd(self._num, self._den)
        self._num //= d
        self._den //= d
        if self._den < 0:
            self._num *= -1
            self._den *= -1

    def __str__(self):
        """
        Return a textual representation of the reduced form of the fraction.
        PRE : The fraction is initialized and reduced
        POST : Return a string in the form 'numerator/denominator' or 'numerator' if the denominator is 1
        RAISES : None
        """
        return f"{self._num}/{self._den}" if self._den != 1 else f"{self._num}"

    def as_mixed_number(self):
        """
        Return a textual representation of the fraction as a mixed number.
        PRE : The fraction is initialized
        POST : Return a string representing the fraction as a mixed number (whole part and fractional part)
        RAISES : None
        """
        if abs(self._num) < self._den:
            return str(self)
        whole = self._num // self._den
        remainder = abs(self._num % self._den)
        if remainder == 0:
            return str(whole)
        return f"{whole} {remainder}/{self._den}"

    def __add__(self, other):
        """
        Add two fractions or a fraction and an integer.
        PRE : self and other are fractions or integers
        POST : Return the sum as a reduced fraction
        RAISES : TypeError if other is not an int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self._num * other._den + other._num * self._den
            den = self._den * other._den
            return Fraction(num, den)
        raise TypeError("You can only add an int or another Fraction.")

    def __sub__(self, other):
        """
        Subtract two fractions or a fraction and an integer.
        PRE : self and other are fractions or integers
        POST : Return the difference as a reduced fraction
        RAISES : TypeError if other is not an int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self._num * other._den - other._num * self._den
            den = self._den * other._den
            return Fraction(num, den)
        raise TypeError("You can only subtract an int or another Fraction.")

    def __mul__(self, other):
        """
        Multiply two fractions or a fraction and an integer.
        PRE : self and other are fractions or integers
        POST : Return the product as a reduced fraction
        RAISES : TypeError if other is not an int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self._num * other._num
            den = self._den * other._den
            return Fraction(num, den)
        raise TypeError("You can only multiply by an int or another Fraction.")

    def __truediv__(self, other):
        """
        Divide two fractions or a fraction and an integer.
        PRE : self and other are fractions or integers, and other is not zero
        POST : Return the quotient as a reduced fraction
        RAISES : ValueError if dividing by zero, TypeError if other is not an int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            if other._num == 0:
                raise ValueError("Cannot divide by zero.")
            num = self._num * other._den
            den = self._den * other._num
            return Fraction(num, den)
        raise TypeError("You can only divide by an int or another Fraction.")

    def __eq__(self, other):
        """
        Check if two fractions or a fraction and an integer are equal.
        PRE : self and other are fractions or integers
        POST : Return True if the fractions or the fraction and integer are equal, otherwise False
        RAISES : TypeError if other is not an int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num == other._num and self._den == other._den
        raise TypeError("You can only compare with an int or another Fraction.")

    def __float__(self):
        """
        Return the float value of the fraction.
        PRE : The fraction is initialized
        POST : Return the float representation of the fraction (numerator/denominator)
        RAISES : None
        """
        return self._num / self._den

    def __lt__(self, other):
        """
        Check if self is less than other.
        PRE : self and other are fractions or integers
        POST : Return True if self is less than other, otherwise False
        RAISES : TypeError if other is not an int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den < other._num * self._den
        raise TypeError("You can only compare with an int or another Fraction.")

    def __le__(self, other):
        """
        Check if self is less than or equal to other.
        PRE : self and other are fractions or integers
        POST : Return True if self is less than or equal to other, otherwise False
        RAISES : TypeError if other is not an int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den <= other._num * self._den
        raise TypeError("You can only compare with an int or another Fraction.")

    def __gt__(self, other):
        """
        Check if self is greater than other.
        PRE : self and other are fractions or integers
        POST : Return True if self is greater than other, otherwise False
        RAISES : TypeError if other is not an int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den > other._num * self._den
        raise TypeError("You can only compare with an int or another Fraction.")

    def __ge__(self, other):
        """
        Check if self is greater than or equal to other.
        PRE : self and other are fractions or integers
        POST : Return True if self is greater than or equal to other, otherwise False
        RAISES : TypeError if other is not an int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den >= other._num * self._den
        raise TypeError("You can only compare with an int or another Fraction.")

    def is_zero(self):
        """
        Check if the fraction is zero.
        PRE : The fraction is initialized
        POST : Return True if the fraction is zero, otherwise False
        RAISES : None
        """
        return self._num == 0

    def is_integer(self):
        """
        Check if the fraction is an integer.
        PRE : The fraction is initialized
        POST : Return True if the fraction is an integer (denominator is 1), otherwise False
        RAISES : None
        """
        return self._den == 1

    def is_proper(self):
        """
        Check if the fraction is a proper fraction.
        PRE : The fraction is initialized
        POST : Return True if the absolute value of the numerator is less than the denominator, otherwise False
        RAISES : None
        """
        return abs(self._num) < self._den

    def is_unit(self):
        """
        Check if the fraction is a unit fraction.
        PRE : The fraction is initialized
        POST : Return True if the fraction is a unit fraction (numerator is 1 and denominator is 1), otherwise False
        RAISES : None
        """
        return abs(self._num) == 1 and self._den == 1

    def is_adjacent_to(self, other):
        """
        Check if the fraction is adjacent to another fraction (i.e., their difference is 1).
        PRE : self and other are fractions or integers
        POST : Return True if the difference between the fractions is 1 (i.e., the fractions differ by 1), otherwise False
        RAISES : TypeError if other is not an int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)

            # Vérifier si other est une fraction
        if isinstance(other, Fraction):
            # Calcul de l'adjacence
            diff = abs(self._num * other._den - other._num * self._den)
            return diff == 1  # Retour explicite de True ou False

            # Lever une exception si other n'est pas valide
        raise TypeError("You can only compare adjacency with an int or another Fraction.")



