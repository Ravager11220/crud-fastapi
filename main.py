from fastapi import FastAPI, Path, Query
from db import dbpy1,dbpy2
from models import Student

app = FastAPI()

#query parameter
@app.get("/secret")
def nn(name : str=None,number : int=None):
    return {"name":name,"number":number}
#path parameter
@app.get("/student/{student_id}")
def gets(student_id : int=None):
    return dbpy1[student_id]
#both query and path parameter
@app.get("/get-data/{students_id}/")
def gd(student_id2: int,students_id:int):
    return {"first-student":dbpy1[students_id],"second-student":dbpy2[student_id2]}

@app.post("/create-student")
def newi(student_no:int , strucn:Student):
    dbpy1[student_no]={"name":strucn}
    return dbpy1[student_no]

@app.delete("/delete")
def dell(st_id:int):
    dbpy1[st_id]={"details":"not-found"}
    return {"status":"deleted"}

@app.put("/update")
def up(stid:int):
    dbpy1[stid]={"details":"updated"}
    return {"status":"updated"}