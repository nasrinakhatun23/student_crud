from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route("/")
def index():
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name")
    if name:
        students.append(name)
    return redirect("/")


@app.route("/delete/<int:id>")
def delete_student(id):
    if id < len(students):
        students.pop(id)
    return redirect("/")

@app.route("/edit/<int:id>")
def edit_student(id):
    return render_template("edit.html", student=students[id], id=id)

@app.route("/update/<int:id>", methods=["POST"])
def update_student(id):
    students[id] = request.form.get("name")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
