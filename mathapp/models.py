from mathapp import db, login_manager
from mathapp import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    points = db.Column(db.Integer(), nullable=False, default=0)

    @property
    def prettier_points(self):
        if len(str(self.points)) >= 4:
            return f'{str(self.points)[:-3]},{str(self.points)[-3:]}'
        else:
            return f"{self.points}"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def add_points(self, exercise):
        self.points += exercise.how_many_points
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'


class Exercise(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=60), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    answer_A = db.Column(db.String(length=60), nullable=False)
    answer_B = db.Column(db.String(length=60), nullable=False)
    answer_C = db.Column(db.String(length=60), nullable=False)
    answer_D = db.Column(db.String(length=60), nullable=False)
    correct_answer = db.Column(db.String(), nullable=False)
    how_many_points = db.Column(db.Integer(), nullable=False, default=10)
