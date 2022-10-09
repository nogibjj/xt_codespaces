echo "The dataset is about Netflix :)"
chmod +x hello_query_sql_db.py
echo "This is dataset overview"

./hello_query_sql_db.py data-intro

echo "Please enter the year you want to query"
read year
./hello_query_sql_db.py query-year --year $year

echo "Let's compare the movie numbers between 2 years, please enter first year"
read year1
echo "Please enter second year"
read year2
./hello_query_sql_db.py year-change --years $year1 $year2