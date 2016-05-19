#!/usr/bin/python
#
import os
import time
class SplitFiles():
	def __init__(self, file_name, line_count=200):
		self.file_name = file_name
		self.line_count = line_count
	def split_file(self):
		start = time.time()
		directory = os.path.dirname(self.file_name)+"/temp_part_file"
		if os.path.exists(directory):
			commend = "rm -r "+directory
			os.system(commend)
		if self.file_name and os.path.exists(self.file_name):
			try:
				with open(self.file_name) as f :
					temp_count = 0
					temp_content = []
					part_num = 0
					for line in f:
						if temp_count < self.line_count:
							temp_count += 1
						else:
							self.write_file(part_num,temp_content)
							part_num += 1
							temp_count = 1
							temp_content = []
						temp_content.append(line)
					else : 
						self.write_file(part_num, temp_content)
			except IOError as err:
				print(err)
		else:
			printf ("%s is not a validate file!\n" %self.file_name)
		end = time.time()
		spend = end - start
		print('spend time %d to divide dictionary\n' %spend)
		return part_num
	def get_part_file_name(self, part_num):
		temp_path = os.path.dirname(self.file_name)
		part_file_name = temp_path + "/temp_part_file"
		if not os.path.exists(part_file_name):
			os.makedirs(part_file_name)
		part_file_name += os.sep + "temp_file_" + str(part_num) + ".txt"
		return part_file_name
	def write_file(self,part_num, *line_content):
		part_file_name = self.get_part_file_name(part_num)
	#	print(line_content)
		try :
	#		print "11" 
			with open( part_file_name, 'w') as part_file:
				part_file.writelines(line_content[0])
	#		print "22"
		except IOError as err:
			print(err)
if __name__ == "__main__":
	sf = SplitFiles(".",100000)
	sf.split_file()
