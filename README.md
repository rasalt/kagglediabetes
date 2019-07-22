Steps 
1. Download the diabetes data set from Kaggle
   link: https://www.kaggle.com/brandao/diabetes/
   Unzip the data set.
      
2. Create your gcs bucket 

   gsutil mb gs://<name>

3. Upload the csv dataset into the gcs bucket 
   gsutil cp diabetic_data.csv gs://<name>/

4. Assuming you have a BQ dataset created , create a new table thus 
   This repo has the schema file created for this data set 
   bq load      --skip_leading_rows=1     --source_format=CSV     <projectname>:<dataset>.<table>     gs://<name>/diabetic_data.csv ./schema.json  

   #If the data was not so dirty I could have used the autodetect feature thus 
   #bq load --autodetect --skip_leading_rows=1     --source_format=CSV     <projectname>:<dataset>.<table>     gs://<name>/diabetic_data.csv 

5. Enjoy exploring your data in BigQuery 
6. Login to your tableau online account using credentials for your account
   Create a new workbook and setup a datasoruce over a BQ connector
6. Login to your tableau online account using credentials for your account
   Create a new workbook and setup a datasoruce over a BQ connector
6. Login to your tableau online account using credentials for your account
   Create a new workbook and setup a datasoruce over a BQ connector
6. Login to your tableau online account using credentials for your account
   Create a new workbook and setup a datasoruce over a BQ connector
6. Login to your tableau online account using credentials for your account
   Create a new workbook and setup a datasoruce over a BQ connector
6. Login to your tableau online account using credentials for your account
   Create a new workbook and setup a datasoruce over a BQ connector
 
