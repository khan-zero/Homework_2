#example using contextlib
#contextlib kutubhonasi yordamidagi code
#installing contextlib in diferet OSes:
#linux:
	#python2: sudo apt-get install python-contextlib2
	#python3: sudo apt-get install python3-contextlib2
#others: pip install contextily

from contextlib import contextmanager

@contextmanager
def custom_list_context():
	items = []
	try:
		yield items
	
	except Exception as e:
		if items:
			items.clear()
		else:
			...
			#"There is nothing 'else' can do" so 'items' is alreadty clean
		print(f"We have faced: {e}")
	
"""\________________main code_______________________/"""

with custom_list_context() as mylist:
	mylist.append(10)
	mylist.append(20)
	mylist.append(30)
	
print(f"Mylist: {mylist}") #output: [10, 20, 30]
