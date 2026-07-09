def calculate_avarage(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def main():
    data = [10,20,30,40,50]
    avg = calculate_avarage(data)
    print(f"AVG: {avg}")
    
if __name__ == "__main__":
    main()