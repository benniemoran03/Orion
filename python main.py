
#### main.py

```python
#!/usr/bin/env python3
import random

def generate_dungeon(width=20, height=10, wall_probability=0.3):
    """
    Generate a dungeon map as a list of strings.
    Each cell is a wall '#' with probability wall_probability, otherwise a floor '.'.
    """
    dungeon = []
    for _ in range(height):
        row = ''.join('#' if random.random() < wall_probability else '.' for _ in range(width))
        dungeon.append(row)
    return dungeon

def print_dungeon(dungeon):
    for row in dungeon:
        print(row)

def main():
    print("Welcome to the Orion Dungeon Generator!")
    dungeon = generate_dungeon()
    print("\nGenerated Dungeon Map:\n")
    print_dungeon(dungeon)

if __name__ == "__main__":
    main()
