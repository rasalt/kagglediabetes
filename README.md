To load the data set into BQ

bq load      --skip_leading_rows=1     --source_format=CSV     dataeng-219316:kagglediabetes.test    gs://kagglediabetes/diabetic_data.csv ./schema.json  

#Data is too dirty to use the autodetect flag. If it was clean the below would have been great !

bq load --autodetect --skip_leading_rows=1  --source_format=CSV     dataeng-219316:kagglediabetes.test0721 gs://kagglediabetes/diabetic_data.csv
