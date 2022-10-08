from unittest import result
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

        # for row in result:
        #     print(row)

    return result

# give a brief introduction of the dataset we are using..
def find_data_intro():
    query = "select count(Name) from default.netflix_1_csv"
    num = querydb(query)
    print("There are " + str(num[0][0]) + " items in this dataset")
    query_sets = "select DISTINCT category from default.netflix_1_csv"
    sets = querydb(query_sets)
    print("The dataset involves " + str(len(sets)) + " categories of movies in Netflix which are: ")
    for row in sets:
        print(row[0])
    query_min = "select min(year) from default.netflix_1_csv"
    min_time = querydb(query_min)
    query_max = "select max(year) from default.netflix_1_csv"
    max_time = querydb(query_max)
    print("Among these movies, oldest is Year " + str(min_time[0][0]) + " and the newest is Year " + str(max_time[0][0]))

def find_most_least_year(year):
    print("------------------")
    query = "select Name, Age_Rating, Duration from default.netflix_1_csv where Year=" + str(year) + " LIMIT 5"
    print("now searching: "+query)
    result = querydb(query)
    for row in result:
        print(row)

def amount_increase(start, end):
    print("------------------")
    query_from = "select count(Name) from default.netflix_1_csv  where Year=" + str(start)
    query_to = "select count(Name) from default.netflix_1_csv  where Year=" + str(end)
    result1 = querydb(query_from)
    result2 = querydb(query_to)
    print("in Year " + str(start) + " There are " + str(result1[0][0]) + " movies")
    print("in Year " + str(end) + " There are " + str(result2[0][0]) + " movies")
    num1 = float(result1[0][0])
    num2 = float(result2[0][0])
    print("The number changes " + str((num2-num1)/num1*100) + "%")