from databricks import sql
import os


def querydb(query="SELECT * FROM default.netflix_1_csv LIMIT 2"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result

def find_most_least_year(year):
    query = "select Name, Age_Rating, Duration from default.netflix_1_csv where Year=" + str(year) + " LIMIT 5"
    print("now searching: "+query)
    querydb(query)