import psycopg


def get_connection():
    connection = psycopg.connect(
        dbname="ai_incident_triage"
    )

    return connection
