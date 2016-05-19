#!/usr/bin/python
import time 
import Queue 
import threading
import hashlib
import getopt
import sys,os,string
passFilename = ''
mylock = threading.RLock()
timeout = 1000
salt = "id14"
#
#----------------------------------------------------------------------------------------------------------------------------------------------------
#  The logical idea of this program as follow:
#	Firstly, use splitfile function to divide our dictionary into small part file
#	Secondly, create many threads to use dictionary and brute force to attack with small part file fo dictionary.
# ---------------------------------------------------------------------------------------------------------------------------------------------------      
# change funciton runs for change e,a of password to 3,4 repectively, and return the value to password
#
#----------------------------------------------------------------------------------------------------------------------------------------------------
def change(value):
	if 'e' in value:
		value = value.replace("e","3")
	if 'a' in value:
		value = value.replace("a","4")
	return value
#----------------------------------------------------------------------------------------------------------------------------------------------------
# this is mainly function to run dictionary and brute force attack.
# Firstly, separate the Md5 code from password.txt
# then exstract value from small part of dictionary to attack
# offer change() and two bytes number brute force to attack
# write the results in crackFile.txt
#
#----------------------------------------------------------------------------------------------------------------------------------------------------
class CrackingMd5(object):
	def __init__(self, filename):
		self.name = filename		
	def work(self):
		passFile = open(passFilename)
		for line in passFile.readlines():
			dictFile = open(self.name,'r')
			if ":" in line:
				user = line.split(':')[0]
				passwd = line.split(':')[1].strip(' ').strip('\n')
			#	 print "Cracking Password for :"+user+"\n"
				for word in dictFile.readlines():
					word = word.strip('\n')
					wordMd5 = hashlib.md5(word).hexdigest()
					if (wordMd5 == passwd):
						PassWd = "Found password for:" +user+"\npassword:"+ word+ "\n"
						mylock.acquire()
						with open("crackFile2.txt", 'a') as f:
							f.write(PassWd)
							f.close()							
						mylock.release()
						break
#					for i in range(10):
#						for j in range(10):
#							word2 = word + str(i)+str(j)
#							word2 = word2.strip(' ')
#							wordMd5 = hashlib.md5(word2).hexdigest()
#							if (wordMd5 == passwd):
#								PassWd = "Found password for:" +user+"\npassword:"+ word+ "\n"
#								mylock.acquire()
#								with open("crackFile.txt", 'a') as f:
#									f.write(PassWd)
#									f.close()
#								mylock.release()
#								break
#						if (wordMd5 == passwd):	
#							break
#					if (wordMd5 == passwd):
#						break
					word1 = change(word)
					wordMd5 = hashlib.md5(word1).hexdigest()
					if (wordMd5 == passwd):
						PassWd = "Found password for:" +user+"\npassword:"+ word+ "\n"
						mylock.acquire()
						with open("crackFile2.txt", 'a') as f:
							f.write(PassWd)
							f.close()
						mylock.release()
						break
#					for i in range(10):
#						for j in range(10):
#							word2 = word1 + str(i)+str(j)
#							word2 = word2.strip(' ')
#							wordMd5 = hashlib.md5(word2).hexdigest()
#							if (wordMd5 == passwd):
#								PassWd = "Found password for:" +user+"\npassword:"+ word+ "\n"
#								mylock.acquire()
#								with open("crackFile.txt", 'a') as f:
#									f.write(PassWd)
#									f.close()
#								mylock.release()
#								break
#						if (wordMd5 == passwd):	
#							break
#					if (wordMd5 == passwd):	
#						break

			#	else: print line+":Password not found in "+self.name+"\n"
		else: print "travesal done in "+self.name+"\n"
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# if the target use the system which is based on Unix system. It will use salt to MD5 as increasing security 
#  I offer this function to decrypt with salt. Others are the same with above function
#
#------------------------------------------------------------------------------------------------------------------------------------------------------------
	def worksalt(self):
		salt = "id14"
		passFile = open(passFilename)
		for line in passFile.readlines():
			dictFile = open(self.name,'r')
			if ":" in line:
				user = line.split(':')[0]
				passwd = line.split(':')[1].strip(' ').strip('\n')
			#	 print "Cracking Password for :"+user+"\n"
				for word in dictFile.readlines():
					word = word.strip('\n')	
					word1 = word + salt
					word1 = word1.strip(' ')				
					wordMd5 = hashlib.md5(word1).hexdigest()
					if (wordMd5 == passwd):
						PassWd = "Found password with salt for:" +user+"\npassword:"+ word+ "\n"
						mylock.acquire()
						with open("crackFile2.txt", 'a') as f:
							f.write(PassWd)
							f.close()
						mylock.release()
						break
#					for i in range(10):
#						for j in range(10):
#							word2 = word + str(i)+str(j)
#							word2 = word2.strip(' ')
#							word3 = word2 + salt
#							wordMd5 = hashlib.md5(word3).hexdigest()
#							if (wordMd5 == passwd):
#								PassWd = "Found password for:" +user+"\npassword:"+ word2+ "\n"
#								mylock.acquire()
#								with open("crackFile.txt", 'a') as f:
#									f.write(PassWd)
#									f.close()
#								mylock.release()
#								break
#						if (wordMd5 == passwd):	
#							break
#					if (wordMd5 == passwd):	
#						break
					word = change(word)
					word1 = word + salt
					word1 = word1.strip(' ')
					wordMd5 = hashlib.md5(word1).hexdigest()
                                        if (wordMd5 == passwd):
                                                PassWd = "Found password with salt for:" +user+"\npassword:"+ word+ "\n"
                                                mylock.acquire()
                                                with open("crackFile2.txt", 'a') as f:
							f.write(PassWd)
							f.close()
						mylock.release()
                                                break
#					for i in range(10):
#						for j in range(10):
#							word2 = word1 + str(i)+str(j)
#							word2 = word2.strip(' ')
#							word3 = word2 + salt
#							wordMd5 = hashlib.md5(word3).hexdigest()
#							if (wordMd5 == passwd):
#								PassWd = "Found password for:" +user+"\npassword:"+ word+ "\n"
#								mylock.acquire()
#								with open("crackFile.txt", 'a') as f:
#									f.write(PassWd)
#									f.close()
#								mylock.release()
#								break
#						if (wordMd5 == passwd):	
#							break
#					if (wordMd5 == passwd):	
#						break
#				else: print line+":Password not found in "+self.name+"\n"
		else: print "travesal done in "+self.name+"\n"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# this is class of thread to crack by thread to save time
#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Thread(threading.Thread):
	def __init__(self,thread_queue):
		self.my_queue = thread_queue
		super(Thread, self).__init__()
	def run(self):
		 while True:
			if self.my_queue.qsize() > 0:
					self.my_queue.get().work()
					self.my_queue.get().worksalt()
			else:
				break
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# usage() function offers the example for command
#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def usage():
	print "Usage Example:\n\n ./CrackingHD5_1py --passwdfile /home/hsu4/cs_577/hw2/password_salt.txt --salt id14 --timeout 60\n(default argument salt == id14, timeout == 1000)\n"
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# main() is used for get and check the options
#
#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
	global passFilename, timeout, salt
	try:
		opts,args = getopt.getopt(sys.argv[1:],"",["passwdfile=","salt=","timeout="])
		for op,value in opts:
			if op == "--passwdfile":
				passFilename = value
			elif op == "--salt":
				salt = value
			elif op == "--timeout":
				timeout = string.atof(value)
	except getopt.GetoptError:
		print "parameter Error!\n"
	if not passFilename.strip():
		print "Please enter file of password.\n"
		usage()
		sys.exit(1)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# this is really main function. SplitFile is the function I write in splitfile.py 
#  it is used for dividing dictionary into small part file. and each file has 1000000 lines
#  then open many thread to attack with small part file of dictionary to save time.
#  use the time.sleep() to control the time to run scripts
#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()
	import splitfile
	sf = splitfile.SplitFiles("./rockyou.txt",line_count=150000)
	file_num = sf.split_file()
	queue_length = file_num + 1
	print ('the number of threads is %d\n' %queue_length)
	my_queue = Queue.LifoQueue(queue_length)
	threads = []
	for i in range(queue_length):
              	file_name = sf.get_part_file_name(i)
                mt = CrackingMd5(file_name)
                my_queue.put_nowait(mt)
        for i in range(queue_length):
                mtd = Thread(my_queue)
                threads.append(mtd)
        for i in range(queue_length):
		threads[i].setDaemon(True)
                threads[i].start()
#		print i
	for i in range(queue_length):
		threads[i].join()
#	time.sleep(timeout)
	print "all done\n"
#	sys.exit(1)			
	

