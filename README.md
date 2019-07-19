To load the data set into BQ

bq load      --skip_leading_rows=1     --source_format=CSV     dataeng-219316:kagglediabetes.test    gs://kagglediabetes/diabetic_data.csv ./schema.json  

