import random

class grid:
    def __init__(self, size: int):
        self.size = size
        self.grid = self.create_grid()

    def create_grid(self) -> list[list[str]]:
        grid = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append('#')
            grid.append(row)
        return grid  # Return the created grid
    
    def print_grid(self):
        for row in self.grid:
            print("".join(row))

    def populate_with_five(self):
        num_changes = random.randint(1, len(self.grid[0]))
        

    
test_grid = grid(10)
test_grid.print_grid()
