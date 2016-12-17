import fileinput
for linenum,line in enumerate( fileinput.FileInput("talent_data/parsed_data.json",inplace=1) ):
   if linenum==0 :
     print("parsed_data =")
     print(line.rstrip())
   else:
     print(line.rstrip())
