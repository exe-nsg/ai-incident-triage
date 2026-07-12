from app.database import get_connection


def seed_services():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO services (name, description)
        VALUES (%s, %s)
        ON CONFLICT (name) DO NOTHING;
        """,
        ("payment-service", "Handles payment processing"),
    )

    connection.commit()

    cursor.close()
    connection.close()

    print("Service inserted successfully")


if __name__ == "__main__":
    seed_services()
