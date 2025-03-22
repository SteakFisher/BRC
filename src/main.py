import math
import sys

def main():
    city_stats = {}
    
    for line in sys.stdin:
        city, score_str = line.strip().split(";")
        score = float(score_str)
        if city in city_stats:
            curr_min, curr_sum, curr_max, count = city_stats[city]
            city_stats[city] = (
                min(curr_min, score),
                curr_sum + score,
                max(curr_max, score),
                count + 1
            )
        else:
            city_stats[city] = (score, score, score, 1)
    
    output_lines = []
    for city in sorted(city_stats.keys()):
        min_score, total_sum, max_score, count = city_stats[city]
        mean_score = math.ceil((total_sum / count) * 10) / 10 
        output_lines.append(f"{city}={min_score:.1f}/{mean_score:.1f}/{max_score:.1f}")
    
    sys.stdout.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    main()