from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """ Redirect to signup route """
    return redirect(url_for('signup'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        form_dict = request.form.to_dict()
        form_val_flag = {}

        def validate_form_str(string):
            """
            Check string for 2 things.
                1. Is greater than 3 char and less than 20 char.
                2. Does not contain space.
            :param string:
            :return 1 or 0:
            """
            if len(string) > 3 and len(string) < 20:
                if ' ' not in string:
                    return 1

            return 0

        def validate_form_verify(verify, password):
            """
            Check if verify and password are the same.
            :param verify:
            :param password:
            :return 1 or 0:
            """
            if verify == password:
                return 1
            else:
                return 0

        def validate_form_email(email):
            """
            Check email for 3 things.
                1. If empty return 1
                2. Check validate_form_str.
                3. Check if '@' and '.' are present.
            :param email:
            :return 1 or 0:
            """
            if email == '':
                return 1
            elif validate_form_str(email):
                if '@' in email and '.' in email:
                    return 1

            return 0

        for (key, value) in form_dict.items():
            """ Flag meaning - 0 is not validated, 1 is validated, and None is empty value but optional"""

            if key == 'username':
                form_val_flag[key] = validate_form_str(value)

                if form_val_flag[key] == 1:
                    username = value
                else:
                    username_error = "That's not a valid username"
                continue

            if key == 'password':
                form_val_flag[key] = validate_form_str(value)

                if not form_val_flag[key] == 1:
                    password_error = "That's not a valid password"
                continue

            if key == 'verify':
                form_val_flag[key] = validate_form_verify(value, form_dict['password'])

                if not form_val_flag[key] == 1:
                    verify_error = "Passwords don't match"
                continue

            if key == 'email':
                form_val_flag[key] = validate_form_email(value)

                if form_val_flag[key] == 1:
                    email = value
                else:
                    email_error = "That's not a valid email"

        if sum(form_val_flag.values()) == 4:
            return redirect(url_for('welcome', username=username))

        return render_template('signup.html', **locals())

    return render_template('signup.html')


@app.route('/welcome')
def welcome():
    username = request.args['username']
    return render_template('welcome.html', username=username)


if __name__ == '__main__':
    app.run()
