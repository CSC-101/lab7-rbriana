import sys


def main():
   total = 0.0




   for arg in sys.argv[1:]:
       try:
           total += float(arg)
       except ValueError:
           print(f"Skipping invalid argument: {arg}")




   print("Sum of valid numbers:", total)


if __name__ == "__main__":
   main()

