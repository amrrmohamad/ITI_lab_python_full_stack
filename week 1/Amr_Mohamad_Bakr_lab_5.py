from flask import Flask, jsonify, request
import sqlite3

database = "test.db"


def connect_db():
    connetion = sqlite3.connect(database)
    connetion.row_factory = sqlite3.Row
    return connetion


# start the database and create the tables in db
def db_creation():
    conn = connect_db()
    conn.execute(
        """
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(255) NOT NULL,
                    age INTEGER ,
                    email VARCHAR(255) NOT NULL
                );
                """
    )
    conn.close()


db_creation()

app = Flask(__name__)

# request -> process[get data,formation ,call ...] -> response


@app.route("/users/", methods=["GET"])
def get_users():
    conn = connect_db()
    data = conn.execute("SELECT * FROM users").fetchall()
    users = [dict(row) for row in data]
    conn.close()
    return jsonify(users)


@app.route("/users/", methods=["POST"])
def insert_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    if name and email:
        conn = connect_db()
        conn.execute("INSERT INTO users (name, email) VALUES (?,?)", (name, email))
        conn.commit()
        conn.close()
        return jsonify({"message": "user inserted successfully"})


# Update an existing To-Do item
@app.route("/users/", methods=["PUT"])
def update_todo(id):
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")

    conn = connect_db()
    users = conn.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()

    if users:
        updated_title = title if title else users["title"]
        updated_description = description if description else users["description"]
        updated_status = status if status else users["status"]

        conn.execute(
            "UPDATE users SET title = ?, description = ?, status = ? WHERE id = ?",
            (updated_title, updated_description, updated_status, id),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "To-Do item updated successfully"})


# Delete a To-Do item
@app.route("/users/", methods=["DELETE"])
def delete_todo(id):
    conn = connect_db()
    users = conn.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()

    if users:
        conn.execute("DELETE FROM users WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "To-Do item deleted successfully"})


app.run(host="0.0.0.0", port=5000)
