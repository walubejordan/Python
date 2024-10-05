class student:
    def __init__(self,name,registration_no,access_no):
        
        self.name = name
        self.registration_no = registration_no
        self.access_no = access_no
    
    def __str__(self):
        return(f"name: {self.name} registration_no: {self.registration_no} access_no: {self.access_no}")

student1 = student("Walube Jordan","S23B13/090","B24795")
student2 = student("Ssenyoga Frank","S23B13/091","B24785")
student3 = student("Lubogo Patrick","S23B13/030","B24789")

print(student1)
print(student2)
print(student3)