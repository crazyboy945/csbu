from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..model.user import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(1, 64)])
    password = PasswordField('口令', validators=[Required()])
    remember_me = BooleanField('记住用户信息')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('电子邮件', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField('用户名', validators=[Required(), Length(1, 64)])
        
        
    #    c, Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
    #                                      '用户名必须由字母、数字, '
    #                                      '点、下划线组成')])
    password = PasswordField('口令', validators=[
        Required(), EqualTo('password2', message='密码不匹配.')])
    password2 = PasswordField('再次输入口令', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮件地址已经注册.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('原口令', validators=[Required()])
    password = PasswordField('新口令', validators=[
        Required(), EqualTo('password2', message='口令必须一致')])
    password2 = PasswordField('再次输入口令', validators=[Required()])
    submit = SubmitField('修改口令')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('电子邮件', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('重置密码')


class PasswordResetForm(FlaskForm):
    email = StringField('电子邮件', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('新口令', validators=[
        Required(), EqualTo('password2', message='口令不一致')])
    password2 = PasswordField('确认口令', validators=[Required()])
    submit = SubmitField('重置口令')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('未知的邮件地址.')


class ChangeEmailForm(FlaskForm):
    email = StringField('新电子邮件', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField('口令', validators=[Required()])
    submit = SubmitField('更新电子邮件')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已经注册.')
