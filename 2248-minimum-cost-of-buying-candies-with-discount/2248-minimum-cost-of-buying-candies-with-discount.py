class Solution:
    def minimumCost(self, cost):
        # Sort the candies in descending order so that we can take the smallest ones for free
        cost.sort(reverse=True)

        total_cost = 0
        # Loop through the sorted list, adding the cost of every candy that is bought
        for i in range(0, len(cost), 3):
            total_cost += cost[i]  # Add the first candy of each group of 3 to total cost
            if i + 1 < len(cost):  # Buy the second candy if available
                total_cost += cost[i + 1]
            # We skip the third candy, as it will be free according to the rules

        return total_cost



