import os
import glob
import pandas as pd
os.chdir("INC")
extension = 'csv'
print("Reading files...")
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
print("Combining files...")
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
print("Converting to csv...")
combined_csv.to_csv( "INC.csv", index=False, encoding='utf-8-sig')

