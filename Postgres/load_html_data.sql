
psql parler_text -U <username> -p 5432 -h parler -c "\copy html_data from '<path/to/csv/parler_text.csv' WITH DELIMITER ',' WITH CSV HEADER"
