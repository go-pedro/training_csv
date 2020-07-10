import csv

#open a csv file
with open ('names.csv','r', newline='') as csv_file:
	csv_reader = csv.reader(csv_file)

	# for line in csv_reader:
	# 	print (line)

	# create csv to write
	with open ('new_names.csv','w',  newline='') as new_csv_file:
		csv_writer=csv.writer(new_csv_file)

		for line in csv_reader:
			csv_writer.writerow(line)


	# next (csv_reader)
	# for line in csv_reader:
	# 	print(line[2])

