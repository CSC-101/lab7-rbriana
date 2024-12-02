from convert import str_to_float


def gather_numbers() -> list[float]:
   numbers = []


   while True:
       user_input = input("Enter a number (or type 'done' to finish): ")


       if user_input.lower() == 'done':
           break


       number = str_to_float(user_input)
       if number is not None:
           numbers.append(number)
       else:
           print("Invalid input. Please enter a valid number.")


   return numbers




if __name__ == '__main__':
   numbers = gather_numbers()
   print("Sum of numbers:", sum(numbers))
