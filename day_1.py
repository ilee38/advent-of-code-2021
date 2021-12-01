from collections import deque


def increasing_depths():
   """
      Part 1 of the puzzle.
   """
   increases_count = 0
   current_depth = float('inf')

   with open("./input.txt") as depths:
      for depth in depths:
         next_depth = int(depth)
         if next_depth > current_depth:
            increases_count += 1
         current_depth = next_depth

   return increases_count


def increasing_sum_of_measurements():
   """
      Part 2 of the puzzle.
   """
   WINDOW_SIZE = 3
   increases_count = 0
   current_sum = float('inf')
   measurement_window = deque()

   with open("./input.txt") as f:
      for _ in range(WINDOW_SIZE):
         measurement_window.append(int(f.readline()))

      next = f.readline()
      while next:
         next_sum = sum(measurement_window)
         if next_sum > current_sum:
            increases_count += 1
         current_sum = next_sum
         measurement_window.popleft()
         measurement_window.append(int(next))
         next = f.readline()
      # Check final sum to avoid off-by-one error
      if len(measurement_window) == 3:
         if sum(measurement_window) > current_sum:
            increases_count += 1

   return increases_count


def main():
   part_1 = increasing_depths()
   part_2 = increasing_sum_of_measurements()

   print(f"Solution to part1: {part_1}")
   print(f"Solution to part2: {part_2}")


if __name__ == "__main__":
   main()