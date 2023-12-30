from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    # id = db.Column(db.Integer <- type of data, primary_key=True <- defining if it has unique ID)
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(
        db.String(100), unique=True
    )  # unique = True means that no other user can have the same email
    password = db.Column(db.String(150))
    company = db.Column(db.String(150))
    jobs = db.relationship("Job")
    clients = db.relationship("Client")
    # two last variables store data for all of users jobs and clients


class Job(db.Model):
    user = db.Column(
        db.Integer, db.ForeignKey("user.id")
    )  # foreign key to reference specific user "ONE TO MANY RELATIONSHIP"
    client = db.Column(
        db.Integer, db.ForeignKey("client.id")
    )  # foreign key to reference specific client
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    job_type = db.Column(db.String(100))
    status = db.Column(db.String(100))
    start_time = db.Column(db.DateTime())
    end_time = db.Column(db.DateTime())
    location = db.Column(db.String(500))
    info = db.Column(db.String(10000))
    lat = db.Column(db.Float())
    lon = db.Column(db.Float())


class Client(db.Model):
    user = db.Column(
        db.Integer, db.ForeignKey("user.id")
    )  # foreign key to reference specific user
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    company = db.Column(db.String(150))
    adress = db.Column(db.String(300))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(250))
    info = db.Column(db.String(10000))

    def __repr__(self):
        return f"<{self.firstname} {self.lastname} {self.company}>"


"""
suggested database structure:
Here's a simplified example of how you might structure your database:

User Table:

Store user information, such as user ID, username, password (hashed), email, etc.
Clients Table:

Each row in this table would be a client, associated with a specific user. You can establish a relationship between the User table and the Clients table using a foreign key that references the user ID.
Jobs Table:

Similar to the Clients table, each row represents a job associated with a specific user. Again, use a foreign key to establish a relationship with the User table.
This way, you can use a single database to manage users, clients, and jobs. The structure might look something like this:

User Table:

UserID (Primary Key)
Username
Password
Email
Other user-related fields
Clients Table:

ClientID (Primary Key)
UserID (Foreign Key referencing User.UserID)
ClientName
ClientDetails
Other client-related fields
Jobs Table:

JobID (Primary Key)
UserID (Foreign Key referencing User.UserID)
ClientID (Foreign Key referencing Clients.ClientID)
JobTitle
JobDescription
Other job-related fields
This structure allows you to associate clients and jobs with specific users while keeping the data organized in a manageable way. The relationships between tables are crucial for maintaining data integrity.

If your web app is expected to handle a large volume of data or requires advanced scalability, you might need to consider additional factors such as database indexing, partitioning, or sharding. However, for many smaller to medium-sized applications, a single database with appropriate table relationships should suffice.
"""
