#Create class HR inheriting Employee. Additional attributes: is_manager, onboard_rate. Method: show_profile that returns {name} has skills: s1, s2. Onboard rate: {onboard_rate}.
class Employee:
    def __init__(self,name,  salary, skill_sets,age):
        self.name=name
        self.salary=salary
        self.skill_sets=skill_sets
        self.age=age
        
    def display_info(self):
        
        
        class HR(Employee):
            def __int__(self,is_manger,onboard_rate):
             self.is_manger=is_manger
             self.onboard_rate=onboard_rate