try:
	file1=open('mailbox.txt')
except:
	print("File cannot be opened or doesn't exist")
	exit()

lines=file1.readlines()
flag=0
file2=open('output.txt','w')
for line in lines:
	if line.startswith("Log:"):
		flag=1
	elif line.startswith('This automatic notification message was sent by') and flag==1:
		flag=0
		file2.write('************************************************************************************************************\n')
	elif not line.startswith('This automatic') and flag==1:
		print(line)
		file2.write(line)
		
file1.close()
