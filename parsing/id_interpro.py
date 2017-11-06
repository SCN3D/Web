#!/usr/bin/python

# Open a file
with open('test2.txt') as fp, open("id_interpro.txt","w") as output:
    for line in fp:
        collapsed = ' '.join(line.split())
        data = collapsed.split(";")
        parsed_1 = data[0].split(" ")
        if parsed_1[0] == "ID" and  id_flag == 0:
            print('id: ',parsed_1[1])
            out_id = parsed_1[1]
		elif parsed_1[0] == "DR" and  parsed_1[1] == "InterPro":
            parsed_2 = data[1].split(" ")
			out_interpro = parsed_2[1]
            print('interPro:  ',parsed_2[1])
            output.write("%s;%s\n" % (out_id,out_go))
output.close()
        
             
            
        
         
