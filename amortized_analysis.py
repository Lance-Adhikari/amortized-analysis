"""Track insertion and copying costs as a dynamic array grows."""

class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity
        self.total_cost = 0

    def push_back(self, value):
        # Count one operation for inserting the new value.
        cost = 1

        # Double the capacity when all slots are occupied.
        if self.size == self.capacity:
            self.capacity = self.capacity * 2
            new_array = [None] * self.capacity

            # Each copied element adds one operation to this insertion.
            for i in range(self.size):
                new_array[i] = self.array[i]
                cost = cost + 1

            self.array = new_array

        # Insert the new element
        self.array[self.size] = value
        self.size = self.size + 1

        # Average the counted operations over all insertions so far.
        self.total_cost = self.total_cost + cost
        amortized_cost = self.total_cost / self.size

        print("Inserted:", value)
        print("Array:", self.array)
        print("Size:", self.size)
        print("Capacity:", self.capacity)
        print("Actual cost:", cost)
        print("Total cost:", self.total_cost)
        print("Amortized cost:", amortized_cost)
        print("--------------------")


def main():
    array = DynamicArray()
    array.push_back(10)
    array.push_back(20)
    array.push_back(30)
    array.push_back(40)
    array.push_back(50)
    array.push_back(60)
    array.push_back(70)
    array.push_back(80)


if __name__ == "__main__":
    main()
