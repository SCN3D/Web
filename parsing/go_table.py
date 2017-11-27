#!/usr/bin/python
with open('test2.txt') as fp, open("go_table.txt","w") as output:
	for line in fp:
		collapsed = ' '.join(line.split())
		data = collapsed.split(";")
		parsed_1 = data[0].split(" ")
		if parsed_1[0] == "DR" and  parsed_1[1] == "GO":
			parsed_2 = data[1].split(" ")
			out_go = parsed_2[1]
			description = data[2] + data[3]
			print('GO:  ',parsed_2[1])
			print('description: ', data[2])
			print('iea: ', data[3])
			output.write("%s;%s\n" % (out_go,description))
	output.close()