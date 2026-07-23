from app.database import get_connection


def create_services_table():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL UNIQUE,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    connection.commit()

    cursor.close()
    connection.close()

    print("services table created successfully")

def create_logs_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id SERIAL PRIMARY KEY,
            service_id INTEGER NOT NULL REFERENCES services(id),
            timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            level VARCHAR(20) NOT NULL,
            message TEXT NOT NULL,
            latency_ms INTEGER
        );
    """)

    connection.commit()

    cursor.close()
    connection.close()

    print("logs table created successfully")

if __name__ == "__main__":
    create_services_table()
    create_logs_table()
