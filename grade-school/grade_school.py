class School:
    def __init__(self):
        self.name = {}

    def add_student(self, name, grade):
        self.name[name] = grade 

    def roster(self):
        l=sorted(self.name.items() ,key=lambda l: l[1])
        l=sorted(l,key= lambda p:(p[1],p[0]))
        return [i[0] for i in l]

    def grade(self, grade_number):
        temp=[]
        for i in self.name:
            if self.name[i]==grade_number:
                temp.append(i)

        return sorted(temp)
