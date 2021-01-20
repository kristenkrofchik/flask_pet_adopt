from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()
db.session.commit()

@app.route('/')
def list_pets():
    """return list of all pets in db with info"""
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/add', methods=['GET'])
def show_add_form():
    """return form to add a pet to app and db"""
    form = AddPetForm()
    return render_template("pet_add_form.html", form=form)

@app.route('/add', methods=['POST'])
def submit_add_form():
    """handle add pet form, add pet to db and app"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data  
        age = form.age.data
        notes = form.notes.data  
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')   
    
    else:
        return render_template("pet_add_form.html", form=form)

@app.route('/<int:pet_id>', methods=['GET'])
def pet_details(pet_id):
    """show pet info and edit form to edit pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    return render_template("pet_detail.html", pet=pet, form=form)

@app.route('/<int:pet_id>', methods=['POST'])
def submit_edit_form(pet_id):
    """handle edit form and update pet info in db and app if needed"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data  
        pet.notes = form.notes.data  
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect('/')   
    
    else:
        return render_template("pet_detail.html", form=form)



    


