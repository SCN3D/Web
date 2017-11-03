#!/usr/bin/python

# Open a file
id_flag = 0
ac_flag = 0
sequence = ''
out_id,out_ac,out_pfam,out_smart,out_prosite,out_supfam = '','','','','',''
with open('test2.txt') as fp, open("output.txt","w") as output:
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
        elif parsed_1[0] == "DR" and  parsed_1[1] == "GO":
            parsed_2 = data[1].split(" ")
            #parsed_3 = data[2].split(" ")
            print('GO:  ',parsed_2[1])
            print('description?: ', data[2])
            print('iea: ', data[3])
        elif parsed_1[0] == "DR" and  parsed_1[1] == "InterPro":
            parsed_2 = data[1].split(" ")
            #parsed_3 = data[2].split(" ")
            print('interPro:  ',parsed_2[1])
            print('description: ', data[2])
        elif parsed_1[0] == "DR" and  parsed_1[1] == "Pfam":
            parsed_2 = data[1].split(" ")
            #parsed_3 = data[2].split(" ")
            out_pfam = parsed_2[1]
            print('Pfam:  ',parsed_2[1])
            print('description: ', data[2])
            print('description: ', data[3])
        elif parsed_1[0] == "DR" and  parsed_1[1] == "PROSITE":
            parsed_2 = data[1].split(" ")
            #parsed_3 = data[2].split(" ")
            out_prosite = parsed_2[1]
            print('Prosite:  ',parsed_2[1])
            print('description: ', data[2])
            print('description: ', data[3])
        elif parsed_1[0] == "DR" and  parsed_1[1] == "SUPFAM":
            parsed_2 = data[1].split(" ")
            #parsed_3 = data[2].split(" ")
            out_supfam = parsed_2[1]
            print('SUPFAM:  ',parsed_2[1])
            print('description: ', data[2])
            print('description: ', data[3])
        elif parsed_1[0] == "SQ" :
            parsed_2 = data[1].split(" ")
            #parsed_3 = data[2].split(" ")
            print('Header:  ',parsed_2[2],';',data[2],';',data[3])
            print('description: ', data[2])
            print('description: ', data[3])
        elif len(parsed_1[0]) > 2:
            sequence += collapsed
        elif parsed_1[0] == '//':
            print(sequence)
            id_flag = 0
            ac_flag = 0
            output.write("%s;%s;%s;%s;%s;%s;%s\n" % (out_id,out_ac,out_pfam,out_smart,out_prosite,out_supfam,sequence))
            sequence = '';
            print('id_flag: ', id_flag, '&ac_flag: ', ac_flag)
            output.close()
        
             
            
        
         
