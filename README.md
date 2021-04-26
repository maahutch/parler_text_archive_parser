# parler_text_archive_parser
Converts the partial parler text archive html files to a csv suitable for loading in a SQL database

## Installation 

1. Clone the repository
2. Inside the repository directory run `pip install -r requirements.txt` to install dependencies
3. Set files paths in `parler_file_path_template.json`. Rename this file to `parler_file_path.txt`.
4. Run `python parler_parse_combo.py`


## Description

The code in this repsository parses the html files in the partial text archive of the website `parler.com` as collected by the hacktivist organization DDoSecrets Collective and produces a unified csv for the entire dataset. The raw data can be accessed here: https://ddosecrets.com/wiki/Parler.  The `Create Table` and `Copy Data` commands for loading the resulting CSV into postgres are available in the `Postgres` directory of this repo. 

  ### Notes: 
* The html files do not contain a calendar data for the post publication. Instead the date is recorded as '1 day ago', '3 weeks ago', '6 months ago' etc. This parser uses this data to estimate the inital publication date assuming the data was collected on January 6th 2021. So, if an html file contains a date field '1 day ago' the csv will contains an 'Estimated Date' value of '01/05/2021'. If you wish to change the starting date from which the Esitmated Date is calulated, the start date variable is created in the file `parse_parler_estimated_date_fun.py`. 
* The 'media' field in the csv will contain any url linked to in the html file. If this url links to an image or video on parler.com, the unique id for that file is stored in the csv column 'video_id'. This id can be matched to the files in the parler video and image archive, also available from the DDoSecrets Collective: https://ddosecrets.com/wiki/Parler
            
            
