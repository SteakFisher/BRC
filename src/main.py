import math
import csv
import sys

def main(input_file_name="testcase.txt", output_file_name="output.txt"):
    city_stats = {}
    
    with open(input_file_name, "r") as input_file:
        reader = csv.reader(input_file, delimiter=";")
        for row in reader:
            city, score_str = row
            city = sys.intern(city) 
            score = float(score_str) 
            if city in city_stats:
                stats = city_stats[city]
                stats[0] = min(stats[0], score)
                stats[1] += score              
                stats[2] = max(stats[2], score)  
                stats[3] += 1                
            else:
                city_stats[city] = [score, score, score, 1]
    
    output_lines = []
    for city in sorted(city_stats.keys()):
        stats = city_stats[city]
        min_score = stats[0]
        total_sum = stats[1]
        max_score = stats[2]
        count = stats[3]
        mean_score = math.ceil((total_sum / count) * 10) / 10
        output_lines.append(f"{city}={min_score:.1f}/{mean_score:.1f}/{max_score:.1f}")
    
    with open(output_file_name, "w") as output_file:
        output_file.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    main()