with open("final.csv", "r") as file:
    # Read the file line by line
    lines = file.readlines()

# Replace all occurrences of blank space with a comma in each line
for i in range(len(lines)):
    maohao = 0
    blank = 0
    sec = 0
    for j in range(len(lines[i])):
        if(lines[i][j]=='"'):
            maohao+=1
            j+=4
            continue
        if(blank==1):
            if (lines[i][j+1]=='('):
                sec = 1
        if((maohao==2) & (lines[i][j]==' ') & (sec==1)):
            blank += 1
            if((blank==2) | (blank==4) | (blank==6)):
                list1 = list(lines[i])
                list1[j]=','
                lines[i]="".join(list1)
        if((maohao==2) & (lines[i][j]==' ') & (sec==0)):
            blank += 1
            if((blank==2) | (blank==3) | (blank==5)):
                list1 = list(lines[i])
                list1[j]=','
                lines[i]="".join(list1)

# Open the file in write mode to overwrite the contents
with open("test.csv", "w") as file:
    # Write the modified lines back to the file
    file.writelines(lines)