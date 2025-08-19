def buzz_number():
    print("🧠 Program: Check Buzz Number")
    print("""\
def is_buzz(num):
    return num % 10 == 7 or num % 7 == 0
""")
    print("🧪 Test Case 1: is_buzz(7) → True")
    print("🧪 Test Case 2: is_buzz(27) → True")
    print("🧪 Test Case 3: is_buzz(19) → False")
    print("📝 Explanation: A Buzz number ends with 7 or is divisible by 7.")


def magic_number():
    print("🧠 Program: Check Magic Number")
    print("""\
def is_magic(num):
    while num > 9:
        num = sum(int(d) for d in str(num))
    return num == 1
""")
    print("🧪 Test Case 1: is_magic(19) → True")
    print("🧪 Test Case 2: is_magic(1234) → False")
    print("📝 Explanation: Keep summing digits until one digit remains. If it is 1 → Magic number.")


def smith_number():
    print("🧠 Program: Check Smith Number")
    print("""\
def sum_digits(n):
    return sum(int(d) for d in str(n))

def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors

def is_smith(num):
    if num < 2:
        return False
    if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
        return False  # prime numbers are not Smith
    return sum_digits(num) == sum(sum_digits(f) for f in prime_factors(num))
""")
    print("🧪 Test Case 1: is_smith(666) → True")
    print("🧪 Test Case 2: is_smith(22) → True")
    print("🧪 Test Case 3: is_smith(13) → False")
    print("📝 Explanation: A composite number where sum of digits equals sum of digits of prime factors.")


def perfect_cubes_range():
    print("🧠 Program: Count Perfect Cubes in a Range")
    print("""\
def perfect_cubes(start, end):
    return [x for x in range(start, end+1) if round(x**(1/3))**3 == x]
""")
    print("🧪 Test Case 1: perfect_cubes(1, 30) → [1, 8, 27]")
    print("🧪 Test Case 2: perfect_cubes(50, 100) → [64]")
    print("📝 Explanation: Checks each number if cube root cubed equals the number.")


def sum_factorials_digits():
    print("🧠 Program: Sum of Factorials of Digits")
    print("""\
import math
def sum_fact_digits(num):
    return sum(math.factorial(int(d)) for d in str(num))
""")
    print("🧪 Test Case 1: sum_fact_digits(145) → 145")
    print("🧪 Test Case 2: sum_fact_digits(123) → 9")
    print("📝 Explanation: Takes each digit, finds factorial, and sums them.")


def median_list():
    print("🧠 Program: Find Median of a List")
    print("""\
def median(lst):
    lst = sorted(lst)
    n = len(lst)
    if n % 2 == 1:
        return lst[n//2]
    else:
        return (lst[n//2 - 1] + lst[n//2]) / 2
""")
    print("🧪 Test Case 1: median([1, 3, 2]) → 2")
    print("🧪 Test Case 2: median([4, 1, 7, 2]) → 3.0")
    print("📝 Explanation: Sorts list and finds middle value (or avg of two if even).")


def peterson_number():
    print("🧠 Program: Check Peterson Number")
    print("""\
import math
def is_peterson(num):
    return sum(math.factorial(int(d)) for d in str(num)) == num
""")
    print("🧪 Test Case 1: is_peterson(145) → True")
    print("🧪 Test Case 2: is_peterson(19) → False")
    print("📝 Explanation: Peterson numbers equal the sum of factorials of their digits.")


def replace_consonants():
    print("🧠 Program: Replace Consonants with #")
    print("""\
def replace_consonants(s):
    vowels = 'aeiouAEIOU'
    return ''.join(ch if ch in vowels or not ch.isalpha() else '#' for ch in s)
""")
    print("🧪 Test Case 1: replace_consonants('Hello') → '#e##o'")
    print("🧪 Test Case 2: replace_consonants('Python') → '#o##o#'")
    print("📝 Explanation: Keeps vowels, replaces consonants with '#'. Non-letters unchanged.")


def sum_alternate_elements():
    print("🧠 Program: Sum of Alternate Elements in a List")
    print("""\
def sum_alternate(lst):
    return sum(lst[::2])
""")
    print("🧪 Test Case 1: sum_alternate([1,2,3,4,5]) → 9")
    print("🧪 Test Case 2: sum_alternate([10,20,30,40]) → 40")
    print("📝 Explanation: Takes elements at indices 0, 2, 4, … and sums them.")


def trimorphic_number():
    print("🧠 Program: Check Trimorphic Number")
    print("""\
def is_trimorphic(num):
    return str(num**3).endswith(str(num))
""")
    print("🧪 Test Case 1: is_trimorphic(4) → True  (4³ = 64)")
    print("🧪 Test Case 2: is_trimorphic(5) → False (5³ = 125)")
    print("📝 Explanation: A number is Trimorphic if its cube ends with the number itself.")