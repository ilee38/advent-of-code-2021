

def horizontal_times_depth():
   """
      Part 1 of the puzzle.
   """
   horizontal_position = 0
   depth = 0

   with open("./input.txt") as steps:
      for step in steps:
         step = step.replace("\n", "")
         if step[0] == "f":
            horizontal_position += int(step[-1])
         elif step[0] == "d":
            depth += int(step[-1])
         elif step[0] == "u":
            depth -= int(step[-1])

   return horizontal_position * depth


def horizontal_times_depth_new():
   """
      Part 2 of the puzzle.
   """
   aim = 0
   horizontal_position = 0
   depth = 0

   with open("./input.txt") as steps:
      for step in steps:
         step = step.replace("\n", "")
         if step[0] == "f":
            horizontal_position += int(step[-1])
            depth += int(step[-1]) * aim
         elif step[0] == "d":
            aim += int(step[-1])
         elif step[0] == "u":
            aim -= int(step[-1])

   return horizontal_position * depth


def main():
   part_1 = horizontal_times_depth()
   print(f'result for part 1: {part_1}')

   part_2 = horizontal_times_depth_new()
   print(f'result for part 2: {part_2}')


if __name__ == "__main__":
   main()