import os
from django.conf import settings

project_root = os.getcwd()[:-8]


# Configuration for the postgresql database
def extract_postgresql():
    import psycopg2

    # Database information
    DB_HOST = settings.DATABASES['default']['HOST']
    DB_NAME = settings.DATABASES['default']['NAME']
    DB_USER = settings.DATABASES['default']['USER']
    DB_PASSWORD = settings.DATABASES['default']['PASSWORD']
    DB_PORT = settings.DATABASES['default']['PORT']

    # Query for everything in `contacts_friends` table
    result_query = "SELECT * FROM contacts_friends"

    # Connection to database
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME,
                            user=DB_USER, password=DB_PASSWORD, port=DB_PORT)

    # Interaction with the database
    db_cursor = conn.cursor()

    file_output_query = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(
        result_query)

    # Output file path
    output_file_location = f'{project_root}\\downloads\\discord_friends.txt'

    with open(output_file_location, 'w', encoding='utf-8') as output:
        db_cursor.copy_expert(file_output_query, output)
