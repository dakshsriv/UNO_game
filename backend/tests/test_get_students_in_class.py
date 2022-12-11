import sqlite3, requests, json

def test_get_students_in_class():
    conn = sqlite3.connect("../classroom.db")
    cursor = conn.cursor()
    x0 = requests.post("https://dev.dakshsrivastava.com/register", json = {"name": "test_get_students_in_clas", "password": "test_get_students_in_clas", "account_type": "Teacher"}, verify=False)
    teacher_id = json.loads(x0.text)["id"]
    x1 = requests.post("https://dev.dakshsrivastava.com/register", json = {"name": "username", "password": "password", "account_type": "Student"}, verify=False)
    student_id = json.loads(x1.text)["id"]
    x2 = requests.post("https://dev.dakshsrivastava.com/classrooms/", json={"title": "test_get_teacher_classrooms", "description": "test_get_teacher_classrooms", "teacher_id":teacher_id}, verify=False)
    class_id = json.loads(x2.text)["id"]
    cursor.execute("INSERT INTO StudentsToClassrooms (STUDENT_ID, CLASSROOM_ID) VALUES (?, ?)", (student_id, class_id))
    conn.commit()
    x = requests.get(f"https://dev.dakshsrivastava.com/classrooms/people/{class_id}", verify=False)
    info = [x[0] for x in json.loads(x.text)]
    cursor.execute("SELECT NAME FROM StudentsToClassrooms JOIN Students ON StudentsToClassrooms.STUDENT_ID=Students.ID WHERE CLASSROOM_ID=? ", (class_id,))
    target = [x[0] for x in cursor.fetchall()]
    cursor.execute("DELETE FROM Classrooms WHERE ID=?", (class_id,))
    cursor.execute("DELETE FROM Teachers WHERE ID=?", (teacher_id,))
    cursor.execute("DELETE FROM Students WHERE ID=?", (student_id,))

    conn.commit()
    conn.close()
    assert (info == target)