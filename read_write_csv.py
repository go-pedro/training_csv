import csv

#open a csv file
with open ('names.csv','r', newline='') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	# for line in csv_reader:
	# 	print (line['email'])

	# create csv to write
	with open ('new_names.csv','w',  newline='') as new_csv_file:
		fieldnames=['first_name', 'last_name', 'email']
		csv_writer=csv.DictWriter(new_csv_file, fieldnames=fieldnames, delimiter='\t')

		csv_writer.writeheader()

		for line in csv_reader:
			csv_writer.writerow(line)


	# next (csv_reader)
	# for line in csv_reader:
	# 	print(line[2])
