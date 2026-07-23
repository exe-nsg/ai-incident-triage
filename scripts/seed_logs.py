from app.database import get_connection


def seed_logs():
    connection = get_connection()
    cursor = connection.cursor()

    # Get the service ID for payment-service
    cursor.execute(
        """
        SELECT id
        FROM services
        WHERE name = %s;
        """,
        ("payment-service",),
    )

    service = cursor.fetchone()

    if service is None:
        cursor.close()
        connection.close()
        print("payment-service not found")
        return

    service_id = service[0]

    # Sample logs
    logs = [
        ("INFO", "Payment request received", 120),
        ("INFO", "Validating payment details", 180),
        ("INFO", "Calling external payment gateway", 450),
        ("WARNING", "Payment gateway response is slow", 1800),
        ("ERROR", "Payment gateway timeout", 5000),
    ]

    # Insert all logs
    cursor.executemany(
        """
        INSERT INTO logs (service_id, level, message, latency_ms)
        VALUES (%s, %s, %s, %s);
        """,
        [
            (service_id, level, message, latency)
            for level, message, latency in logs
        ],
    )

    connection.commit()

    cursor.close()
    connection.close()

    print("Logs inserted successfully")


if __name__ == "__main__":
    seed_logs()
