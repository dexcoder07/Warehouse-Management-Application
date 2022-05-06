from flask import render_template, flash, redirect, url_for
from company.models import Login, Details, Chlorine,Hydrogen,Oxygen,Plant
from company import app, db
from company.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Login.query.filter_by(id=form.emp_id.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash('You are successfully signed in', category='success')
            if form.designation.data=='Administrator' or form.designation.data=='administrator':
                return redirect(url_for('admin_view'))
            if form.designation.data=='Supervisor' or form.designation.data=='supervisor':
                return redirect(url_for('supervisor_view'))
        else:
            flash('Employee ID and Password are not matched! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        L_user = Login(id = form.emp_id.data,
                       password=form.password.data,
                       location=form.location.data,
                       designation=form.designation.data)
        E_D = Details(e_id=L_user,
                          name=form.name.data,
                          address=form.address.data,
                          phone_number=form.ph_no.data,
                          email_id=form.email_address.data)

        db.session.add(L_user)
        db.session.add(E_D)
        db.session.commit()
    if form.errors != {}: #if there are not errors from the validations
        for err_mssg in form.errors.values():
            flash(f'There was an error with creating a user: {err_mssg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/supervisor')
def supervisor():
    return render_template('supervisor.html')


@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home"))

@app.route('/supervisor_view')
def supervisor_view():
    return render_template('supervisor.html')


@app.route('/admin_view')
def admin_view():
    return render_template('admin.html')

@app.route('/plant_view')
def plant_view():

    plt = Plant.query.all()
    return render_template('plant_view.html', plant = plt)

@app.route('/chlorine')
def chlorine():
    chlorines = Chlorine.query.all()
    return render_template('chlorine.html',chlorine = chlorines)

@app.route('/hydrogen')
def hydrogen():
    hyd = Hydrogen.query.all()
    return render_template('hydrogen.html' ,hydrogen = hyd)

@app.route('/oxygen')
def oxygen():
    oxy = Oxygen.query.all()
    return render_template('oxygen.html',oxygen = oxy)
