import pandas as pd

# Adding a "CPT Group" field to the dataset
expanded_data_with_cpt = {
    "Code": [
        "G89.29", "M54.5", "G89.18", "R51.9", "M47.892", "M50.30", "R07.9",
        "K21.9", "M25.561", "R10.84", "J45.909", "I25.10", "N39.0", "M54.2",
        "M54.9", "R10.9", "R53.1", "K35.80", "R19.7", "G43.909", "G89.3",
        "M54.41", "G89.21", "R52", "M47.894", "M50.20", "R10.13", "K21.0",
        "M25.562", "R10.10", "J44.9", "I48.91", "N13.2", "M54.6", "R11.2",
        "R53.0", "K40.90", "R63.4", "G44.1", "G89.4"
    ],
    "Description": [
        "Other chronic pain", "Low back pain", "Other acute postprocedural pain", "Headache, unspecified", 
        "Other spondylosis, cervical region", "Cervical disc disorder, unspecified", "Chest pain, unspecified", 
        "Gastro-esophageal reflux disease without esophagitis", "Pain in right knee", "Abdominal tenderness, unspecified site", 
        "Unspecified asthma, uncomplicated", "Atherosclerotic heart disease of native coronary artery without angina pectoris", 
        "Urinary tract infection, site not specified", "Cervicalgia", "Dorsalgia, unspecified", "Abdominal pain, unspecified", 
        "Weakness", "Unspecified acute appendicitis", "Diarrhea, unspecified", "Migraine, unspecified, not intractable, without status migrainosus",
        "Neoplasm related pain (acute) (chronic)", "Lumbago with sciatica, right side", "Chronic pain syndrome", "Pain, unspecified", 
        "Other spondylosis, lumbar region", "Cervical disc disorder with myelopathy, unspecified", "Epigastric pain", 
        "Gastro-esophageal reflux disease with esophagitis", "Pain in left knee", "Right upper quadrant pain", 
        "Chronic obstructive pulmonary disease, unspecified", "Unspecified atrial fibrillation", "Hydronephrosis with renal and ureteral calculous obstruction", 
        "Pain in thoracic spine", "Nausea and vomiting", "Malaise and fatigue", "Unilateral inguinal hernia, without obstruction or gangrene, not specified as recurrent", 
        "Abnormal weight loss", "Vascular headache, not elsewhere classified", "Chronic pain due to trauma"
    ],
    "Status": ["Active"] * 40,
    "Specialty": [
        "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", 
        "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", 
        "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", 
        "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", 
        "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", 
        "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia", 
        "Anesthesia", "Anesthesia", "Anesthesia", "Anesthesia"
    ],
    "Duration": ["Variable"] * 40,
    "Type": ["ICD-10"] * 40,
    "Terminology":  [
        "Chronic Pain", "Low Back Pain", "Acute Pain", "Headache", 
        "Spondylosis", "Cervical Disc Disorder", "Chest Pain", 
        "GERD", "Knee Pain", "Abdominal Tenderness", 
        "Asthma", "Heart Disease", "UTI", "Neck Pain", 
        "Back Pain", "Abdominal Pain", "Weakness", 
        "Appendicitis", "Diarrhea", "Migraine", 
        "Neoplasm Pain", "Lumbago with Sciatica", "Chronic Pain Syndrome", "General Pain", 
        "Spondylosis", "Cervical Myelopathy", "Epigastric Pain", "GERD with Esophagitis", 
        "Knee Pain", "RUQ Pain", "COPD", "Atrial Fibrillation", "Hydronephrosis", 
        "Thoracic Spine Pain", "Nausea and Vomiting", "Malaise and Fatigue", "Inguinal Hernia", 
        "Weight Loss", "Vascular Headache", "Chronic Pain due to Trauma"
    ],
    "CPT Group": [
        "00100-01999", "62263-62284", "01916-01936", "99100-99140", 
        "01951-01953", "01935-01936", "99143-99150", "99116-99140", 
        "62310-62319", "01960-01969", "01951-01953", "01991-01992", 
        "99100-99140", "01999", "99100-99140", "01960-01969", 
        "62263-62284", "01960-01969", "62263-62284", "01951-01953", 
        "00100-01999", "01916-01936", "62263-62284", "99100-99140", 
        "01951-01953", "01935-01936", "99143-99150", "99116-99140", 
        "62310-62319", "01960-01969", "01951-01953", "01991-01992", 
        "99100-99140", "01999", "99100-99140", "01960-01969", 
        "62263-62284", "01960-01969", "62263-62284", "01951-01953"
    ]
}

# Create a DataFrame with the additional "CPT Group" column
expanded_df = pd.DataFrame(expanded_data_with_cpt)

# Save to an Excel file

expanded_file_path = "icd10_for_Anesthesia_40_codes.xlsx"
expanded_df.to_excel(expanded_file_path, index=False)

# Save to an CSV file
expanded_file_path = "icd10_for_Anesthesia_40_codes.csv"
expanded_df.to_csv(expanded_file_path, index=False)

expanded_file_path
