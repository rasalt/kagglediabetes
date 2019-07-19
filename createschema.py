columns1 = ["encounter_id","patient_nbr"]
columns2 = ["race","gender","age","weight"]
columns3 = ["admission_type_id","discharge_disposition_id","admission_source_id","time_in_hospital","payer_code"]
columns4 = ["medical_specialty"]
columns5 = ["num_lab_procedures","num_procedures","num_medications","number_outpatient","number_emergency","number_inpatient","diag_1","diag_2","diag_3","number_diagnoses","max_glu_serum","A1Cresult"]
columns6 = ["metformin","repaglinide","nateglinide","chlorpropamide","glimepiride","acetohexamide","glipizide","glyburide","tolbutamide","pioglitazone","rosiglitazone","acarbose","miglitol","troglitazone","tolazamide","examide","citoglipton","insulin","glyburide_metformin","glipizide_metformin","glimepiride_pioglitazone","metformin_rosiglitazone","metformin_pioglitazone","change","diabetesMed","readmitted"]
#2278392","8222157","Caucasian","Female","["0-10)","?","6","25","1","1","?","Pediatrics-Endocrinology","41","0","1","0","0","0","250.83","?","?","1","None","None","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","NO
#149190","55629189","Caucasian","Female","["10-20)","?","1","1","7","3","?","?","59","0","18","0","0","0","276","250.01","255","9","None","None","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","No","Up","No","No","No","No","No","Ch","Yes",">30

#with open("schema.json","w+") as f:
#  f.write("[") 
#  for name in columns1: 
#    f.write(" {")
#    f.write("   \"description\": \"{}\".format(name))","
#    f.write("   \"name\": \"{}\".format(name))","
#    f.write("   \"type\": \"String\")","
#  f.write(" }",")
#  f.write("]") 

with open("schema.json","w+") as f: 
    f.write("[\n") 
    for name in columns1: 
        f.write(" {\n")
        f.write("   \"description\": \"{}\",\n".format(name)),
        f.write("   \"name\": \"{}\",\n".format(name)),
        f.write("   \"type\": \"Integer\"\n"),
        f.write(" },\n",)
    for name in columns2: 
        f.write(" {\n")
        f.write("   \"description\": \"{}\",\n".format(name)),
        f.write("   \"name\": \"{}\",\n".format(name)),
        f.write("   \"type\": \"String\"\n")
        f.write(" },\n",)
    for name in columns3: 
        f.write(" {\n")
        f.write("   \"description\": \"{}\",\n".format(name)),
        f.write("   \"name\": \"{}\",\n".format(name)),
        f.write("   \"type\": \"Integer\"\n"),
        f.write(" },\n",)
    for name in columns4: 
        f.write(" {\n")
        f.write("   \"description\": \"{}\",\n".format(name)),
        f.write("   \"name\": \"{}\",\n".format(name)),
        f.write("   \"type\": \"String\"\n"),
        f.write(" },\n",)
    for name in columns5: 
        f.write(" {\n")
        f.write("   \"description\": \"{}\",\n".format(name)),
        f.write("   \"name\": \"{}\",\n".format(name)),
        f.write("   \"type\": \"Integer\"\n"),
        f.write(" },\n",)
    for name in columns6: 
        f.write(" {\n")
        f.write("   \"description\": \"{}\",\n".format(name)),
        f.write("   \"name\": \"{}\",\n".format(name)),
        f.write("   \"type\": \"String\"\n"),
        f.write(" },\n",)

    f.write("]") 
