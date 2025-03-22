import math

def main(input_file_name="testcase.txt", output_file_name="output.txt"):
    city_stats = {}
    
    with open(input_file_name, "r") as input_file:
        for line in input_file:
            city, score_str = line.strip().split(";")
            score = float(score_str)
            if city in city_stats:
                curr_min, curr_sum, curr_max, count = city_stats[city]
                city_stats[city] = (min(curr_min, score), curr_sum + score, max(curr_max, score), count + 1)
            else:
                city_stats[city] = (score, score, score, 1)
    
    output_lines = []
    for city in sorted(city_stats):
        min_score, total_sum, max_score, count = city_stats[city]
        mean_score = math.ceil((total_sum / count) * 10) / 10
        output_lines.append("%s=%.1f/%.1f/%.1f" % (city, min_score, mean_score, max_score))
    
    with open(output_file_name, "w") as output_file:
        output_file.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    main()