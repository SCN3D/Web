#!/usr/bin/python

# Open a file
with open('uniprot_sprot.txt') as fp, open("prosite_table.csv","w") as output:
	for line in fp:
		collapsed = ' '.join(line.split())
		data = collapsed.split(";")
		parsed_1 = data[0].split(" ")
		if parsed_1[0] == "DR" and  parsed_1[1] == "PROSITE":
			parsed_2 = data[1].split(" ")
			out_prosite = parsed_2[1]
			description = data[2] + data[3]
			print('Prosite:  ',parsed_2[1])
			print('description: ', data[2])
			print('description: ', data[3])
			output.write("%s,%s\n" % (out_prosite,description))
output.close()
