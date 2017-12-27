#!/usr/bin/python

# Open a file
with open('1.txt') as fp, open("id_prosite.csv","w") as output:
	for line in fp:
		collapsed = ' '.join(line.split())
		data = collapsed.split(";")
		parsed_1 = data[0].split(" ")
		if parsed_1[0] == "ID":
			print('id: ',parsed_1[1])
			out_id = parsed_1[1]
		if parsed_1[0] == "DR" and  parsed_1[1] == "PROSITE":
			parsed_2 = data[1].split(" ")
			out_prosite = parsed_2[1]
			print('Prosite:  ',parsed_2[1])
			output.write("%s,%s\n" % (out_id,out_prosite))
output.close()

