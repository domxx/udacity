#!/usr/bin/python3
import psycopg2
import time

db = psycopg2.connect(dbname="postgres", user="", password="")
cur = db.cursor()
cur.execute("""
    SELECT title, COUNT (title) as views
    FROM articles
    JOIN log ON CONCAT('/article/', slug) = path
    GROUP BY title
    ORDER BY views DESC
    LIMIT 3
""")
res = cur.fetchall()
print("\nTask 1:")
for item in res:
    print("{} - {} views".format(item[0], item[1]))

cur.execute("""
    SELECT COUNT (title) as views, authors.name
    FROM articles
    JOIN log ON CONCAT('/article/', slug) = path
    JOIN authors ON authors.id = articles.author
    GROUP BY authors.name
    ORDER BY views DESC
""")
res = cur.fetchall()
print("\nTask 2:")
for item in res:
    print("{} - {} views".format(item[1], item[0]))

cur.execute("""
    SELECT
        a.days,
        ROUND (
            (b.count::numeric / (a.count::numeric / 100)),
            2)
        AS
            percentage
        FROM
            (SELECT TO_CHAR(time, 'Mon DD, YYYY') as days, COUNT(time) as count
            FROM log
            GROUP BY days) AS a
    JOIN
        (SELECT TO_CHAR(time, 'Mon DD, YYYY') as days, COUNT(time) as count
        FROM log
        WHERE status != '200 OK'
        GROUP BY days
        ORDER BY days) AS b
    ON
        a.days = b.days
    WHERE
        (a.count / 100) < b.count
""")
data = cur.fetchall()

print("\nTask3:")
for item in data:
    print("{} - {}% errors".format(item[0], item[1]))