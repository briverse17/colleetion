class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # monitor the chef's availability
        prev = 0
        # total waiting time of all customers
        total_wait = 0
        for arrive, time in customers:
            # if it's the first customer
            # or if the customer arrives
            # when the chef is free
            # let him prepare the food immediately
            prev = max(prev, arrive)

            # update the chef's finishing time
            prev += time
            # and customers' waiting time
            wait = prev - arrive
            total_wait += wait

        # average waiting time
        return total_wait / len(customers)
