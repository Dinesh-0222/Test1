import queue as q
patient_name = q.Queue()
def register():
          name=input("Enter the patient's name: ")
          patient_name.put(name)
def display():
          dis=patient.get()
          printt(dis)
def remove():
          if not patient_name.empty():
                              patient_name.get()
                              print("Patient Remove successfully")
print("Enter the option\n1.Register new patient\n2.Remove Patient\n3.View Patient\n4.Exit")
opt=int(input("Enter the Option: \n"))
i=10
while i>0:
          if opt==1:
                    register()
          elif opt==2:
                    remove()
          elif opt==3:
                    display()
          elif opt==4:
                    print("Thank you for the services")