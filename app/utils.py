import re


def extract_stress_score(text: str):
    """
    Extract stress score from AI response

    Example:
    Stress Level: 8/10
    """

    try:

        lines = text.split("\n")

        for line in lines:

            if "stress level" in line.lower():

                numbers = re.findall(r"\d+", line)

                if numbers:

                    score = int(numbers[0])

                    if score > 10:
                        score = 10

                    return score

    except Exception:
        pass

    return 5


def calculate_burnout_risk(entries):

    if not entries:
        return "Low"

    scores = []

    for entry in entries:

        analysis = entry.get("analysis", "")

        score = extract_stress_score(analysis)

        scores.append(score)

    if not scores:
        return "Low"

    avg = sum(scores) / len(scores)

    if avg >= 8:
        return "High"

    if avg >= 5:
        return "Medium"

    return "Low"


def get_stress_trend(entries):

    trend = []

    for entry in entries:

        score = extract_stress_score(
            entry.get("analysis", "")
        )

        trend.append(
            {
                "date": entry["date"][:10],
                "score": score
            }
        )

    return trend


def detect_common_triggers(entries):

    triggers = {
        "mock tests": 0,
        "peer comparison": 0,
        "parents": 0,
        "family pressure": 0,
        "exam fear": 0,
        "self doubt": 0,
        "burnout": 0,
        "rank": 0,
        "sleep": 0
    }

    for entry in entries:

        text = (
            entry.get("journal", "")
            + " "
            + entry.get("analysis", "")
        ).lower()

        for trigger in triggers:

            if trigger in text:
                triggers[trigger] += 1

    return dict(
        sorted(
            triggers.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )


def average_stress(entries):

    if not entries:
        return 0

    scores = []

    for entry in entries:

        score = extract_stress_score(
            entry.get("analysis", "")
        )

        scores.append(score)

    return round(
        sum(scores) / len(scores),
        2
    )


def emergency_warning(text: str):

    text = text.lower()

    danger_words = [
        "suicide",
        "kill myself",
        "self harm",
        "hopeless",
        "end my life",
        "can't go on"
    ]

    for word in danger_words:

        if word in text:
            return True

    return False