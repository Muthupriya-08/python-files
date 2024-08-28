from flask import Flask,render_template,request,redirect,url_for,flash
import mysql.connector


app=Flask(__name__)
app.secret_key='your_secret_key'


host = '127.0.0.1'
user = 'root'
password = 'Muthupriya_08'
database = 'muthudb'


connection = mysql.connector.connect(
   host=host,
   user=user,
   password=password,
   database=database
)

cursor = connection.cursor()

@app.route('/')

def index():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET','POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']
        insert_query = 'INSERT INTO students (name, age, course) VALUES (%s, %s, %s)'
        data= (name, age, course)
        cursor.execute(insert_query, data)
        connection.commit()

        flash('Student added successfully', 'success')
        return redirect(url_for('index'))

    return render_template('add_student.html')

if __name__=='__main__':
    app.run(debug=True)
