from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=128)])
    description = TextAreaField('Description')
    due_date = DateField('Due Date', validators=[DataRequired()])
    completed = BooleanField('Completed')
    submit = SubmitField('Submit')