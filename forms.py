from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitFields

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Las contraseñas no son iguales')
    ])
    confirm = PasswordField('Repetir password')
    submit = SubmitFields('Registrarse')
