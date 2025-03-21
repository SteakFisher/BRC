import math

def main(input_file_name="testcase.txt", output_file_name="output.txt"):
    city_scores = {}
    
    with open(input_file_name, "r") as input_file:
        for line in input_file:
            city, score = line.strip().split(";")
            score = float(score)
            if city not in city_scores:
                city_scores[city] = []
            city_scores[city].append(score)
    city_stats = {}
    for city, scores in city_scores.items():
        min_score = min(scores)
        max_score = max(scores)
        mean_score = sum(scores) / len(scores)
        mean_score = math.ceil(mean_score * 10) / 10 
        city_stats[city] = (min_score, mean_score, max_score)
    
    with open(output_file_name, "w") as output_file:
        for city in sorted(city_stats.keys()):
            min_score, mean_score, max_score = city_stats[city]
            output_line = f"{city}={min_score:.1f}/{mean_score:.1f}/{max_score:.1f}\n"
            output_file.write(output_line)

if __name__ == "__main__":
    main()