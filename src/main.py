import math
import multiprocessing as mp

def worker(queue, stats_dict):
    """Worker process to process lines from the queue and update statistics."""
    while True:
        line = queue.get()
        if line is None:
            break
        city, score = line.strip().split(";")
        score = float(score)
        if city in stats_dict:
            curr_min, curr_sum, curr_max, count = stats_dict[city]
            stats_dict[city] = (
                min(curr_min, score),
                curr_sum + score,
                max(curr_max, score),
                count + 1
            )
        else:
            stats_dict[city] = (score, score, score, 1)

def main(input_file_name="testcase.txt", output_file_name="output.txt"):
    """Main function to process city scores and write statistics."""
    num_workers = mp.cpu_count()
    queue = mp.Queue()
    manager = mp.Manager()
    stats_dicts = [manager.dict() for _ in range(num_workers)]
    workers = []
    for i in range(num_workers):
        p = mp.Process(target=worker, args=(queue, stats_dicts[i]))
        p.start()
        workers.append(p)
    
    with open(input_file_name, "r") as input_file:
        for line in input_file:
            queue.put(line)
    
    for _ in range(num_workers):
        queue.put(None)
    
    for p in workers:
        p.join()
    
    aggregated_stats = {}
    for stats in stats_dicts:
        for city, (min_s, sum_s, max_s, count_s) in stats.items():
            if city in aggregated_stats:
                curr_min, curr_sum, curr_max, curr_count = aggregated_stats[city]
                aggregated_stats[city] = (
                    min(curr_min, min_s),
                    curr_sum + sum_s,
                    max(curr_max, max_s),
                    curr_count + count_s
                )
            else:
                aggregated_stats[city] = (min_s, sum_s, max_s, count_s)

    output_lines = []
    for city in sorted(aggregated_stats.keys()):
        min_score, total_sum, max_score, count = aggregated_stats[city]
        mean_score = math.ceil((total_sum / count) * 10) / 10 
        output_lines.append(f"{city}={min_score:.1f}/{mean_score:.1f}/{max_score:.1f}")
    
    with open(output_file_name, "w") as output_file:
        output_file.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    main()