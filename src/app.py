from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from flask_mysqldb import MySQL

app = Flask(__name__)
# mysql database
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "Universidad"

mysql = MySQL(app)
app.secret_key="mysecretkey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=[ "POST"])
def login():
    if request.method == "POST":
        user_id = request.form["username"]
        contra = request.form["contraseña"]
        print ("usuario ",user_id, contra)
        cur = mysql.connection.cursor()
        cur2 = mysql.connection.cursor()
        #cur2 = mysql.connection.cursor()
        #cur3 = mysql.connection.cursor()
        #cur.execute("select id from cliente where email = %s",{em2})
        #id_user = cur.fetchall()[0][0]
        #datos del usuario
        query = "select username, password from profesores ;"
        cur.execute(query)
        profesores_v = cur.fetchall() 

        query2 = "select username, password from alumnos ;"
        cur2.execute(query2)
        alumnos_v = cur2.fetchall() 
        #where email = %s and contrasena = %s",{em2,contra2})        
        user=None
        contrasena=None
        user2=None
        contrasena2=None

        for user_, contrasena_ in profesores_v:
            if user_ == user_id and contrasena_ == contra:
                user = user_
                contrasena = contrasena_
                print (user," **", contrasena)
        
        for user2_, contrasena2_ in alumnos_v:
            if user2_ == user_id and contrasena2_ == contra:
                user2 = user2_
                contrasena2 = contrasena2_
                print (user2," **", contrasena2)

        #print(usuario, contraseña)
        if (user == user_id and contrasena == contra) or (user2 == user_id and contrasena2 == contra):
            if (user == user_id and contrasena == contra):
                return redirect (url_for("login_profesor"))
            else:
                return redirect (url_for("login_alumno"))
        else:
            return "Contraseña incorrecta"
            flash("usuario no existente")


@app.route("/cuenta/")
def cuenta():
    return render_template("selec_cuenta.html")


@app.route("/alumno/")
def alumno():
    return render_template("alumno.html")


@app.route("/login_alumno/")
def login_alumno():
    return render_template("login_alumno.html")

@app.route("/add_alumno", methods=["POST"])
def add_alumno():
        if request.method == "POST":
            nom = request.form["nombre"]
            cod_ = request.form["codigo"]
            user = request.form["username"]
            contra = request.form["password"]
            
            cur2 = mysql.connection.cursor()
            cur2.execute("select username from profesores")
            profesores = cur2.fetchall()

            cur3 = mysql.connection.cursor()
            cur3.execute("select username from alumnos")
            alumnos = cur3.fetchall()
            user_profesor=None
            user_alumno=None
            
            #print(str(users))
            #for email in users :
             #   if (email[0] == em):
              #      print("correo existe")
               #     return "El correo ya existe"
            
            for user_ in profesores :
                if (user_[0] == user):
                    user_profesor = user_[0]
            for user2_ in alumnos:
                if (user2_[0] == user):
                    user_alumno = user2_[0]

            if user_profesor == user or user_alumno == user:  
                return redirect(url_for("alumno"))
            print("INSERT", id, nom, cod_, user, contra)
            cur = mysql.connection.cursor()
            cur.execute("insert into alumnos(nombre, codigo, username, password) values(%s,%s,%s,%s)", (nom, cod_, user, contra))
            mysql.connection.commit()
            flash("Contacto Insertado Correctamente")
            return redirect (url_for("index"))
        return "alumno"

@app.route("/profesor/")
def profesor():
    return render_template("profesor.html")

@app.route("/login_profesor/")
def login_profesor():
    return render_template("login_profesor.html")

@app.route("/add_profesor", methods=["POST"])
def add_profesor():
        if request.method == "POST":
            nom = request.form["nombre"]
            cod_ = request.form["codigo"]
            user = request.form["username"]
            contra = request.form["password"]
            
            cur2 = mysql.connection.cursor()
            cur2.execute("select username from profesores")
            profesores = cur2.fetchall()

            cur3 = mysql.connection.cursor()
            cur3.execute("select username from alumnos")
            alumnos = cur3.fetchall()
            user_profesor=None
            user_alumno=None
            
            #print(str(users))
            #for email in users :
             #   if (email[0] == em):
              #      print("correo existe")
               #     return "El correo ya existe"
            
            for user_ in profesores :
                if (user_[0] == user):
                    user_profesor = user_[0]
            for user2_ in alumnos:
                if (user2_[0] == user):
                    user_alumno = user2_[0]

            if user_profesor == user or user_alumno == user:  
                return redirect(url_for("profesor"))
            print("INSERT", id, nom, cod_, user, contra)
            cur = mysql.connection.cursor()
            cur.execute("insert into profesores(nombre, codigo, username, password) values(%s,%s,%s,%s)", (nom, cod_, user, contra))
            mysql.connection.commit()
            flash("Contacto Insertado Correctamente")
            return redirect (url_for("index"))
        return "profesor"









if __name__=="__main__":
    app.run(port=3000, debug=True)
