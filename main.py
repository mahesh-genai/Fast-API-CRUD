from fastapi import FastAPI,HTTPException
from model import Employee

Employee_db:list[Employee]=[] 

app= FastAPI()

##read all emp

@app.get("/Employee", response_model=list[Employee]) 
def get_employees():
    return Employee_db


##read specific
@app.get("/employee/{emp_id}", response_model=Employee)
def get_employee(emp_id:int):
    for index,employee in enumerate (Employee_db):
        if employee.id==emp_id:
            return Employee_db[index]
    raise HTTPException(status_code=404, detail="employe not found")

##add a employee

@app.post("/add_employee", response_model=Employee)
def add_employee(new_emp:Employee):
    for employee in Employee_db:
        if employee.id==new_emp.id:
            raise HTTPException(status_code="400", detail="already exist")
    Employee_db.append(new_emp)
    return new_emp

##update a perticuler emp

@app.put("/update_employee/{emp_id}", response_model=Employee)
def update_employee(emp_id:int, updated_emp:Employee):
    for index,Employee in enumerate (Employee_db):
        if Employee.id==emp_id:
            Employee_db[index]=updated_emp
            return updated_emp
        
    raise HTTPException(status_code="404", detail="emp not found")

##delete emp

@app.delete("/delete_employee/{emp_id}", response_model=Employee)
def delete_employee(emp_id:int):
    for index, employee  in enumerate (Employee_db) :
        if employee.id == emp_id:
            del Employee_db[index]
            return {"msg":"emp deleted successfully"}
        
        raise HTTPException(status_code=404, detail="empoyee not found")
        



