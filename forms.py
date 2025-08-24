from flask_wtf import FlaskForm
import wtforms


class SingUpForm(FlaskForm):
    username = wtforms.StringField(
        label="Логін",
        validators = [wtforms.validators.DataRequired(), wtforms.validators.length(min=3)]
)
    password = wtforms.PasswordField(
        label="Пароль",
        validators = [wtforms.validators.DataRequired(), wtforms.validators.length(min=6)]
)
    fullname = wtforms.StringField(label="Ваше повне ім'я (за бажанням)")
    phone_number = wtforms.StringField(label="Ваш номер телефону (за бажанням)")
    submit = wtforms.SubmitField(label="Зареєструватись")


class SingInForm(FlaskForm):
    username = wtforms.StringField(
        label="Логін",
        validators = [wtforms.validators.DataRequired(), wtforms.validators.length(min=3)]
    )
    password = wtforms.PasswordField(
        label="Пароль",
        validators = [wtforms.validators.DataRequired(), wtforms.validators.length(min=6)]
    )
    submit = wtforms.SubmitField(label="Вхід")


class ContactForm(FlaskForm):
    first_name = wtforms.StringField(label="Ім'я", validators=[wtforms.validators.DataRequired()])
    last_name = wtforms.StringField(label="Прізвище", validators=[wtforms.validators.DataRequired()])
    phone_number = wtforms.StringField(label="Номер телефону", validators=[wtforms.validators.DataRequired()])
    city = wtforms.StringField(label="Місто (необов'язково)")
    bio = wtforms.StringField(label="Додаткова інформація (необов'язково)")
    file = wtforms.FileField(label="Фото контакта (необов'язково)")
    submit = wtforms.SubmitField(label="Додати контакт")
