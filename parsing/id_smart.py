#!/usr/bin/python

# Open a file
with open('uniprot_sprot.txt') as fp, open("id_smart.csv","w") as output:
	for line in fp:
		collapsed = ' '.join(line.split())
		data = collapsed.split(";")
		parsed_1 = data[0].split(" ")
		if parsed_1[0] == "ID":
			print('id: ',parsed_1[1])
			out_id = parsed_1[1]
		if parsed_1[0] == "DR" and  parsed_1[1] == "SMART":
			parsed_2 = data[1].split(" ")
			out_smart = parsed_2[1]
			print('SMART:  ',parsed_2[1])
			output.write("%s,%s\n" % (out_id,out_smart))
output.close()
