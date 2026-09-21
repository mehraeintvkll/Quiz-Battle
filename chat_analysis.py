import json
import sys
from collections import Counter, defaultdict

CHAT_PATH = "chat.json"


def load_messages(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def messages_per_person(messages: list[dict]) -> Counter:
    return Counter(m["from"] for m in messages)


def busiest_hours(messages: list[dict]) -> tuple[list[int], int]:
    """ساعت(های) شلوغ‌ترین زمان و تعداد پیام در آن ساعت را برمی‌گرداند."""
    per_hour = Counter(int(m["time"].split(":")[0]) for m in messages)
    peak = max(per_hour.values())
    hours = sorted(h for h, c in per_hour.items() if c == peak)
    return hours, peak


def average_length_per_person(messages: list[dict]) -> dict[str, float]:
    lengths = defaultdict(list)
    for m in messages:
        lengths[m["from"]].append(len(m["text"]))
    return {name: sum(l) / len(l) for name, l in lengths.items()}


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else CHAT_PATH
    messages = load_messages(path)
    total = len(messages)

    print(f"تعداد کل پیام‌ها: {total}\n")

    print("=== تعداد پیام هر نفر ===")
    for name, count in messages_per_person(messages).most_common():
        print(f"{name}: {count} پیام ({count / total * 100:.1f}%)")

    print("\n=== شلوغ‌ترین زمان چت ===")
    hours, peak = busiest_hours(messages)
    for h in hours:
        print(f"ساعت {h:02d}:00 تا {h:02d}:59 ({peak} پیام)")

    print("\n=== میانگین طول پیام (تعداد کاراکتر) ===")
    averages = average_length_per_person(messages)
    for name, avg in sorted(averages.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {avg:.1f}")


if __name__ == "__main__":
    main()