# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/
# Time Complexity - O(n log n) due to sorting the cars based on their position
# Space Complexity - O(n) for the list of cars and the variables used in the algorithm
# Category - Array
# Hint - Sort the cars based on their position in descending order, then iterate through the sorted list of cars and calculate the time it takes for each car to reach the target, if the time for the current car is greater than the time for the previous car, then it forms a new fleet, otherwise it joins the fleet of the previous car, we can keep track of the number of fleets and the time for the previous car, at the end we return the number of fleets

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet = 0

        # zip function is used to combine the position and speed lists into a list of tuples,
        # sort the list of tuples based on the position in descending order, this way we can iterate through the cars from the closest to the target to the farthest, this is important because if a car is closer to the target than another car, it will reach the target faster and will form a fleet with the other car if they have the same time to reach the target
        # sample input - target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
        # after zip and sort - cars = [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
        cars = sorted((zip(position, speed)), reverse=True)
        hrs_left_previous_car = 0

        for x in cars:
            hrs_left = (target - x[0]) / x[1]  # formula = (target - position) / speed

            if hrs_left_previous_car < hrs_left:
                fleet += 1
                hrs_left_previous_car = hrs_left

        return fleet