from app.database import get_connection


def read_logs():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM logs;
        """
    )

    logs = cursor.fetchall()

    cursor.close()
    connection.close()

    normal_count = 0
    warning_count = 0
    critical_count = 0

    for log in logs:
        log_id = log[0]
        service_id = log[1]
        timestamp = log[2]
        level = log[3]
        message = log[4]
        latency = log[5]

        if level == "ERROR":
            critical_count += 1
            print(f"Critical Incident: {message}")

        elif level == "WARNING" and latency > 1000:
            warning_count += 1
            print(f"Performance Incident: {message}")

        else:
            normal_count += 1
            print(f"Normal: {message}")
    print()
    print("=" * 40)
    print("Incident Summary")
    print("=" * 40)
    print(f"Normal Logs: {normal_count}")
    print(f"Warning Incidents: {warning_count}")
    print(f"Critical Incidents: {critical_count}")
    print("=" * 40)


if __name__ == "__main__":
    read_logs()
