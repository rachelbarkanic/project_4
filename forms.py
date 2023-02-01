from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class TeamForm(FlaskForm):
    team_name = StringField('Team Name', validators=[DataRequired(), Length(min = 4, max = 255)])
    submit = SubmitField('Submit')

class ProjectForm(FlaskForm):
    project_name = StringField('Project Name', validators=[DataRequired(), Length(min = 4, max = 255)])
    description = TextAreaField('Please Enter a Description')
    completed = BooleanField('Has This Project Been Completed?')
    team_selection = SelectField('Team')
    submit = SubmitField('Submit')

    def update_teams(self, teams):
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams ]

class DeleteForm(FlaskForm):

    project_name = StringField('Name of Project to Delete: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

    
