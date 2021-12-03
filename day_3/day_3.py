def initialize_count_dict(size):
   counts = {}
   for i in range(size):
      counts[i] = [0] * 2

   return counts


def gamma_epsilon_rates(counts):
   gamma = "0b"
   epsilon = "0b"

   for i in range(len(counts.keys())):
      if counts[i][0] > counts[i][1]:
         gamma += "0"
         epsilon += "1"
      else:
         gamma += "1"
         epsilon += "0"

   return gamma, epsilon


def get_power_consumption():
   """
      Part 1 of the puzzle.
   """
   #Number of bits in the input numbers
   WORD_SIZE = 12
   counts = initialize_count_dict(WORD_SIZE)

   with open("./input.txt") as numbers:
      for number in numbers:
         number = number.replace("\n", "")
         for i in range(WORD_SIZE):
            if number[i] == "0":
               counts[i][0] += 1
            elif number[i] == "1":
               counts[i][1] += 1

   gamma_rate , epsilon_rate = gamma_epsilon_rates(counts)

   return int(gamma_rate, 2) * int(epsilon_rate, 2)


def main():
   part_1 = get_power_consumption()
   print(f"result for part 1: {part_1}")


if __name__ == "__main__":
   main()