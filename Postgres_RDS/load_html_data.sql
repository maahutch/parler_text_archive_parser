
psql parler_text -U postgres -p 5432 -h <AWS RDS DATABASE>.rds.amazonaws.com -c "\copy html_data from '<Location of your CSV>/parler_output.csv' WITH CSV HEADER"