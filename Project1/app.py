from flask import Flask,render_template,request
app = Flask(__name__)

class StudentGrading:
    def __init__(self):
        self.students = {}
    def calculate_grade(self,marks):
        if marks>=90:
            return "A+"
        elif marks>=75:
            return "A"
        elif marks>=60:
            return "B"
        elif marks>=50:
            return "C"
        else:
            return "F"
    def add_student(self,roll,name,marks):
        grade = self.calculate_grade(marks)
        self.students[roll] = {
            'name' : name,
            'marks' : marks,
            'grade' : grade
        }
    def get_student(self,roll):
        return self.students.get(roll)
obj = StudentGrading()

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        roll = int(request.form.get('roll'))
        name = request.form.get('name')
        marks = float(request.form.get('marks'))

        obj.add_student(roll,name,marks)
        student = obj.get_student(roll)
        return render_template('result.html',roll=roll,name=student['name'],marks=student['marks'],grade=student['grade'])
    return render_template('index.html')

@app.route('/view',methods=['POST','GET'])
def view():
    if request.method == 'POST':
        roll = int(request.form.get('roll'))
        student = obj.get_student(roll)
        if not student:
            return "STudent not found!!"
        return render_template('result.html',roll=roll,name=student['name'],marks=student['marks'],grade=student['grade'])
    return render_template('view.html')

@app.route('/all')
def all():
    return render_template('all.html',students=obj.students)

if __name__=='__main__':
    app.run(debug=True)