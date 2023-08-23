#!/usr/bin/env python3
class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
  ]


    def __init__(self, name, job):
        self.name = name
        self.job = job

    def get_name (self):
        return self.name
    
    def get_job (self):
        return self.job

    def set_name (self, new_name):
        new_name = new_name.title()
        if isinstance(new_name, str) and (1<= len(new_name) <=25):
            print(f"new set name is {new_name}")
            self.name = new_name
        else:
            print("Name must be string under 25 characters.")  

    new_name = property(get_name, set_name,) 


    def set_job (self , new_job):
        if new_job in self.APPROVED_JOBS :
            print (f"new set job is {new_job}") 
            self.job = new_job 
        else:
            print("Job must be in list of approved jobs.") 

    new_job = property(get_job, set_job,)                     

me= Person("ali", "pilot")
print(me.name)
print(me.job)
me.new_name = "jabir"
me.new_job = "Admin"
