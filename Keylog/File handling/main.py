#File_handling
f=open("log.txt",'a')
f.write("\n who are you bro?")
f.close
# r=read
# a=append(used in this project)
# w=write

#with_keyword (closes file automatically)
with open("log.txt",'a') as f:
    f.write("\n who are you ?")