import sys
# Tar argument från os och passar till scriptet.
if len(sys.argv) != 3:
  exit('please pass filepath and action')
file_path = sys.argv[1]
action = sys.argv[2]

# Loopa igenom filen och hitta [x], indexera två variabler, lägg ihop dem och ta bort newlines .
def print_notice():
  with open(file_path) as file:
    for line in file:
      if '[notice]' in line:
        date_start = line[1:25]
        message_start = line[35:]
        print((date_start + message_start).replace("\n", ""))
        
# Loopa igenom filen och hitta [x], indexera två variabler, lägg ihop dem och ta bort newlines .                
def print_errors():
  with open(file_path) as file:
    for line in file:
      if '[error]' in line:
        date_start = line[1:25]
        message_start = line[34:]
        print((date_start + message_start).replace("\n", ""))
        
# Loopa igenom filen och hitta [x], checka att den har hittats, räkna antal gånger [x]
def print_statistics():
  total=0
  with open(file_path) as file:
    for line in file:
      found = line.find("[error]")
      if found != -1:
        total+=1
  print ("errors", total )
  
# Loopa igenom filen och hitta [x], checka att den har hittats, räkna antal gånger [x]  
def print_statistics2():
  total=0
  with open(file_path) as file:
    for line in file:
      found = line.find("[notice]")
      if found != -1:
        total+=1
  print ("notices", total)
   
# Printa två funktioner på var sin rad                              
def stats ():
  print_statistics() 
  print_statistics2()
   
# Kontroll för systemargument 
if action == "notice":
  print_notice ()
elif action == "error":
  print_errors ()
elif action == "statistics":
  stats()
else: 
  print("Invalid command")