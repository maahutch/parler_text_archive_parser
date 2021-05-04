CREATE DATABASE parler; 

CREATE TABLE html_data ( 
		title varchar, 
		echoed varchar, 
		createdDateTime varchar, 
		estimatedDate DATE,
		author varchar, 
		username varchar, 
		impressions varchar, 
		body varchar, 
		media varchar, 
		parlerMediaFileId varchar,
		htmlFileName varchar
); 

\copy html_data from '<path/to/csv/parler_text.csv' WITH DELIMITER ',' CSV HEADER;

ALTER TABLE html_data ADD COLUMN id SERIAL PRIMARY KEY;





