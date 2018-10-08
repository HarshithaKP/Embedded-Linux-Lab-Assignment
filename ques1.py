import sys

def ipmatch():
	ip=sys.argv[1]
	count=0
	print(ip)
	fileopen=open("ip.txt","r")
	iplist=fileopen.readlines()
	for line in iplist:
		line=line.split(' ')
		print(line)
		for i in range(0,len(line)):
			if(line[i]==ip):
				count=count+1
			
	
	print("The IP match count :")
	print(count)
	fileopen.close()
			
def main():
	ipmatch();

if __name__ == '__main__':
	main()