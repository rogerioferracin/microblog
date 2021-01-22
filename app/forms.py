from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_('Username')), validators=[DataRequired()])
    password = PasswordField(_('Password')), validators=[DataRequired()])
    remember_me = BooleanField(_('Remember Me'))
    submit = SubmitField(_('Sign In'))

class RegistrationForm(FlaskForm):
    username = StringField(_('Username')), validators=[DataRequired()])
    email = StringField(_('Email')), validators=[DataRequired(), Email()])
    password = PasswordField(_('Password')), validators=[DataRequired()])
    password2 = PasswordField(
        _('Repeat password')), validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField(_('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username'))
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please user a different email'))
        

class EditProfileForm(FlaskForm):
    username = StringField(_('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_('About me'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
    
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username = self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username'))


class EmptyForm(FlaskForm):
    submit = SubmitField(_('Submit'))


class PostForm(FlaskForm):
    post = TextAreaField(_('Say something'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_('Submit'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_('Email')), validators=[DataRequired(), Email()])
    submit = SubmitField(_('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_('Password')), validators=[DataRequired()])
    password2 = PasswordField(_('Password')), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_('Request Password Reset'))
