from collections import Counter

def count_and_sort_duplicate_lines(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]  # Remove empty lines and whitespace

    line_counts = Counter(lines)

    # Keep only lines that occur more than once
    duplicates = {line: count for line, count in line_counts.items() if count > 1}

    # Sort duplicates by count (descending)
    sorted_duplicates = sorted(duplicates.items(), key=lambda x: x[1], reverse=True)

    print("Duplicate Lines (sorted by frequency):")
    for line, count in sorted_duplicates:
        print(f'"{line}" appears {count} times')

    print(f"\nTotal number of duplicate lines: {len(sorted_duplicates)}")
    print(f"\n Total lines: ",len(lines))

# Example usage
file_path = 'xx'  # Replace with your actual file path
count_and_sort_duplicate_lines(file_path)

