 
with open("New_file2.txt",'w') as f:
    for i in range(10):
        f.write("This is line {}\n".format(i+2))
    f.seek(11)
    f.write("Modified****")
    print(f.tell())

          