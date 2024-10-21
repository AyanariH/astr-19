import numpy as np

def generate_sin_table():
    
    num_entries = 1000
    x_min = 0
    x_max = 2
    
    
    step_size = (x_max - x_min) / (num_entries - 1)
    
    
    sin_table = []
    for i in range(num_entries):
        x = x_min + i * step_size
        sin_x = np.sin(x)
        sin_table.append((x, sin_x))
    
    return sin_table

def print_sin_table(sin_table):
    
    print(f"{'x':>10} {'sin(x)':>10}")
    print('-' * 22)
    
    
    for x, sin_x in sin_table:
        print(f"{x:10.5f} {sin_x:10.5f}")

def main():
    sin_table = generate_sin_table()
    print_sin_table(sin_table)

if __name__ == "__main__":
    main()