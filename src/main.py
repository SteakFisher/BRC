import math

def main(input_file_name="testcase.txt", output_file_name="output.txt"):
    city_stats = {}
    
    with open(input_file_name, "r") as input_file:
        for line in input_file:
            city, score = line.strip().split(";")
            score = float(score)
            if city in city_stats:
                curr_min, curr_sum, curr_max, count = city_stats[city]
                city_stats[city] = (min(curr_min, score), curr_sum + score, max(curr_max, score), count + 1)
            else:
                city_stats[city] = (score, score, score, 1)
    
    with open(output_file_name, "w") as output_file:
        for city in sorted(city_stats):  # O(k log k)
            min_score, total_sum, max_score, count = city_stats[city]
            mean_score = math.ceil((total_sum / count) * 10) / 10
            output_file.write(f"{city}={min_score:.1f}/{mean_score:.1f}/{max_score:.1f}\n")

if __name__ == "__main__":
    main()