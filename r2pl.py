from prettytable import PrettyTable
res_table = PrettyTable()
log_table = PrettyTable()

class transaction:
	def __init__(self,a,b,c):
		self.op = a
		self.t = b
		self.v = c

res_table.field_names = ["Resource", "Status", "Transaction"]
log_table.field_names = ["Log","Table","2PL"]

schedule = []
temp = str(input("Enter the operations\nGuide:\nr: read\nw: write\n1-9:transaction id\nAt last mention the variable on which transaction is working\nCommit: C1C\nAbort:A1A\nExample: r1x w1x r2y\n"))

for x in range(0,len(temp)-1,4):
	schedule.append(transaction(temp[x],temp[x+1],temp[x+2]))

wait = []
resources = []
waiting_trans = []
current = 0  #This is our pointer to operations
free_vars = []
u= 0

def res_status(a):
	for x in resources:
		if x[0] == a:
			return x  #return the status of resource
		else:
			continue
	resources.append([a,0,0])   #If resouce is not in the resource list then add it
	res_table.add_row([a,"Free",0])
	return resources[len(resources)-1]


def get_index(a):
	#print("Get Index Called") ######################
	c = 0
	for x in resources:
	#	print(x[0],"check equal to ",a)
		if x[0] == a:
			return c
		else:
			c=c+1
			continue
	return c

def grant_sl(a,b):
	#print("before",resources) ########
	if(a in free_vars):
		free_vars.remove(a)
	#print("Index is ",get_index(a))  ###########
	resources[get_index(a)]=[a,1,b]
	print("Shared lock on",a, "---> T",b,"           |")
	res_table.add_row([a,"Shared",b])
	log_table.add_row(["Shared Lock",a,b])
	#print("after",resources) ######
	
def grant_xl(a,b):
	if(a in free_vars):
		free_vars.remove(a)
	#print("This is index",get_index(a)) #########
	resources[get_index(a)]=[a,2,b]
	#print(resources[get_index(a)]) ###############3
	print("Exclusive lock on",a, "---> T",b,"        |")
	res_table.add_row([a,"Exclusive",b])
	log_table.add_row(["Exclusive Lock",a,b])


def release_locks(b):
	#print("RELEASED CALLED") ###########################################
	for x in resources:
		if x[2] == b:    #We find all the resources allocated to transaction passed to this function
	#		print(x) ##########################
			x[1] = 0     #Make resource status 0 (idle)
			x[2] = 0     #Release the resource from that transaction
			free_vars.append(x[0])
	#		print(x)  ########################################
		else:
			continue

def iswaiting(a):
	for x in waiting_trans:
		if x == a:
			return True
		else:
			continue
	return False

def ifalld():
	c = True
	for x in schedule:
		if x.op == "d":
			continue
		else:
			c = False
	return c        

print("\n---------Rigorous-2PL-LOG------------+")
print("                                     |")

x = 0

while  x < len(schedule):
	if schedule[x].op == "d":
		x=x+1
		continue

	if iswaiting(schedule[x].t):
		x = x+1
		continue

	elif schedule[x].op == "r":
		temp = res_status(schedule[x].v)
		if temp[1] == 0:           #Case : Resource is Free
			grant_sl(schedule[x].v,schedule[x].t)
			schedule[x].op = "d"
			x = x+1
			continue
			#schedule.remove(schedule[x])
		elif temp[2] == schedule[x].t: #Resource is already with same transaction
			schedule[x].op = "d"
			#schedule.remove(schedule[x])
			x = x+1
			continue
		elif temp[2] != schedule[x].t:
			wait.append([schedule[x].t,x,schedule[x].v]) #So if transaction is to be kept in wait state we store trans id, index at which the command is skipped and resource for which it is waiting
			waiting_trans.append(schedule[x].t)
			print("Transaction",schedule[x].t,"--> WAIT           |")
			log_table.add_row(["WAIT","-",schedule[x].t])
		else:
			print("Dont Print 1")

	elif schedule[x].op == "w":
		temp = res_status(schedule[x].v)
		if temp[1] == 0:
		#	print(temp)#########
			grant_xl(schedule[x].v,schedule[x].t)
			schedule[x].op = "d"
			x = x+1
			continue
			#schedule.remove(schedule[x])
		elif temp[2] == schedule[x].t and temp[1] == 2:
			schedule[x].op = "d"
			x = x+1
			continue
			#schedule.remove(schedule[x])
		elif temp[2] == schedule[x].t and temp[1] == 1:
		#	print("THis this") #########################################
			grant_xl(schedule[x].v,schedule[x].t)
			schedule[x].op = "d"
			x = x+1
		#	print(temp)#########
			continue
			#schedule.remove(schedule[x])
		elif temp[2] != schedule[x].t:
			wait.append([schedule[x].t,x,schedule[x].v])
			waiting_trans.append(schedule[x].t)
			print("Transaction",schedule[x].t,"--> WAIT               |")
	#		print(waiting_trans)      #########################################################
			log_table.add_row(["WAIT","-",schedule[x].t])
		else:
			print("Dont Print 2")

	elif schedule[x].op == "C" or "A":
		if schedule[x].op == "C":
	#		print(waiting_trans) #########################################
			print("Transaction",schedule[x].t,"--> COMMITED           |")
			log_table.add_row(["COMMIT","-",schedule[x].t])
		elif schedule[x].op == "A":
			print("Transaction",schedule[x].t,"--> ABORTED            |")
			log_table.add_row(["ABORT","-",schedule[x].t])
		schedule[x].op = "d"
	#	print(schedule[x].t) #########################
		release_locks(schedule[x].t)
	#	print(len(waiting_trans),"Hello") ################################
		if len(waiting_trans) != 0:
			for w in wait:
	#			print(w,"Hello 1") ##############################
				#print(free_vars) ##########################
				for z in free_vars:
					if w[2] == z:
						print("Transaction",w[0],"--> RESCHEDULED        |")
						log_table.add_row(["RESCHEDULED","-",w[0]])
						u = w[1]
						wait.remove(w)
						#free_vars.clear()
	#					print(w[2],"Idharr") ###########3
						free_vars.remove(w[2])
						waiting_trans.remove(w[0])
						break
					else:
						continue

			x = u
		elif len(waiting_trans)==0 and ifalld():
			print("                                     |")
			print("-----------------EXIT----------------+\n")
			break
		#else:
		#   print("Dont Print This")
	#elif schedule:
	#   x = 0
	#   continue

print(res_table)
print(log_table)

#r1a,w2a,C1C,r2b,w3a,r2a,w3b,r3c,C3C,C2C



