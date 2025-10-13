import math # to be able to use math function like math.ceil

class Pagination: # Step 1: Create a class pagination
    def __init__(self, items=None, page_size=10):
        # Step 2: Initialize
        if items is None: # behavior
            items = []
        self.items = items
        self.page_size = page_size
        self.current_idx = 0 # current page index
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        # Step 3: Return visible items based on current page index
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # Step 4: Navigation methods
    def go_to_page(self, page_num):
        if not (1 <= page_num <= self.total_pages):
            raise ValueError("Page number out of range.")
        self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # Bonus Step 5: __str__ method
    def __str__(self):
        return "\n".join(self.get_visible_items())


# Step 6: Test Cases
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

try:
    p.go_to_page(10)
except ValueError as e:
    print(e)
# Output: ValueError

try:
    p.go_to_page(0)
except ValueError as e:
    print(e)
# Output: ValueError

# Test the __str__ method
p.first_page()
print(str(p))
# a
# b
# c
# d