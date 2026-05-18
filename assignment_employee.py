class employee:
    def __init__(self,id:str,name:str):
        self.id = id
        self.name = name
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def info (self):
        return f"Id:{self.id}\nName: {self.name}"
    def cal_sel(self):
        return "no salary ye to calculate"
    
class part_time(employee):
    def __init__(self,id,name,hourly_rate:float,worked_hour:int):
        employee.__init__(self,id,name)
        self.hourly_rate = hourly_rate
        self.worked_hour = worked_hour
    def cal_sal(self):
        return f"part time salary: {self.hourly_rate * self.worked_hour}"
    def info (self):
        return f"Id:{self.id}\nName: {self.name}\npart time Salary: {self.hourly_rate *self.worked_hour}"


class full_time(employee):
    def __init__(self,id:str,name:str,fixed:int,bonus:float):
        employee.__init__(self,id,name)
        self.fixed = fixed
        self.bonus = bonus
    def cal_sal(self):
        return f"full time salary: {self.fixed + self.bonus}"
    def info (self):
        return f"Id:{self.id}\nName: {self.name}\nFull time Salary: {self.fixed +self.bonus}"

class contractor(employee):
    def __init__(self,id:str,name:str,daily_rate:float,days_worked:int):
        employee.__init__(self,id,name)
        self.daily_rate = daily_rate
        self.days_worked = days_worked
    def __str__(self):
        return f"{self.id}, {self.name}, {self.daily_rate}, {self.days_worked}"
    def cal_sal(self):
        return f"contractor salary: {self.daily_rate * self.days_worked}"
    def info (self):
        return f"Id:{self.id}\nName: {self.name}\ncontractor Salary: {self.daily_rate *self.days_worked}"



con= contractor("001","ahmed",170.6,17)
fu_t = full_time("002","ali",26000,17000)
# print(fu_t.cal_sal())
# print(con.info())
# print(con.get_id())
# print(con.cal_sal())
print(con)