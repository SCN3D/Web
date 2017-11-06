#!/usr/bin/python

# Open a file
with open('test2.txt') as fp, open("interpro_table.txt","w") as output:
    for line in fp:
        collapsed = ' '.join(line.split())
        data = collapsed.split(";")
        parsed_1 = data[0].split(" ")
		if parsed_1[0] == "DR" and  parsed_1[1] == "InterPro":
            parsed_2 = data[1].split(" ")
            out_interpro = parsed_2[1]
			description = data[2]
            print('interPro:  ',parsed_2[1])
            print('description: ', data[2])
            output.write("%s;%s\n" % (out_interpro,description))
output.close()
        
             
            
        
         
