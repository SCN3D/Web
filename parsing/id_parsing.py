#!/usr/bin/python

# Open a file
id_flag = 0
ac_flag = 0
sequence = ''
with open('test2.txt') as fp, open("id.txt","w") as output:
    for line in fp:
        collapsed = ' '.join(line.split())
        data = collapsed.split(";")
        parsed_1 = data[0].split(" ")
        if parsed_1[0] == "ID" and  id_flag == 0:
            id_flag = 1
            print('id: ',parsed_1[1])
            out_id = parsed_1[1]
		elif parsed_1[0] == "AC" and  ac_flag == 0:
            ac_flag = 1
            print('ac 1: ',parsed_1[1])
            out_ac = parsed_1[1]
            if len(data)  > 2:
                for x in range(1, len(data)-1):
                    print('ac', x+1,': ', data[x])
                    out_ac += data[x]
        elif len(parsed_1[0]) > 2:
            sequence += collapsed
        elif parsed_1[0] == '//':
            print(sequence)
            id_flag = 0
            ac_flag = 0
            output.write("%s;%s;%s\n" % (out_id,out_ac,sequence))
            sequence = '';
            print('id_flag: ', id_flag, '&ac_flag: ', ac_flag)
output.close()
        
             
            
        
         
