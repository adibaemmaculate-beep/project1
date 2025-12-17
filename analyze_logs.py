from collections import defaultdict


def parse_log_line(line):
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None

    date = parts[0]
    time = parts[1]
    level = parts[2]
    message = parts[3]

    return date, time, level, message


def analyze_logs(file_path):
    event_counts = defaultdict(int)
    error_messages = defaultdict(int)
    total_lines = 0

    with open(file_path, "r") as file:
        for line in file:
            parsed = parse_log_line(line)
            if not parsed:
                continue

            _, _, level, message = parsed
            total_lines += 1
            event_counts[level] += 1

            if level == "ERROR":
                error_messages[message] += 1

    return total_lines, event_counts, error_messages


def generate_summary(total_lines, event_counts, error_messages):
    with open("summary.txt", "w") as f:
        f.write("Log Analysis Summary\n")
        f.write("--------------------\n")
        f.write(f"Total log entries: {total_lines}\n\n")

        f.write("Event counts:\n")
        for level, count in event_counts.items():
            f.write(f"- {level}: {count}\n")

        f.write("\nRepeated errors:\n")
        for message, count in error_messages.items():
            if count > 1:
                f.write(f"- {message} ({count} occurrences)\n")


def main():
    total_lines, event_counts, error_messages = analyze_logs("logs.txt")
    generate_summary(total_lines, event_counts, error_messages)


if __name__ == "__main__":
    main()
