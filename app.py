from flask import Flask , render_template , url_for , request , redirect , session
from userService import userService
app = Flask(__name__)
app.secret_key = 'sdasdad'

@app.route('/' , methods=['GET','POST'])
def index() :

    # Login Process
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = userService(username,password)
        if user.login() == 1:
            session['username'] = user.username
            session['password'] = user.password
        else :
            message = 'Login gagal, username/password salah'
            return render_template('index.html', error=message)

    # if user still login , automatically redirecting to page /<username>/cashier
    if 'username' in session :
        return redirect(url_for('cashier',username=session['username']))

    return render_template('index.html')

@app.route('/<username>/cashier', methods=['GET','POST'])
def cashier(username) :
    user = userService(session['username'],session['password'])

    if 'serial_number' in session :
        return redirect(url_for('invoice'))

    if 'error' in session :
        error = session['error']
        session.pop('error',None)
        return render_template('cashier.html',
            username=user.username, 
            food=user.food[user.username], 
            food_amount= len(user.food[user.username]['food_name']),
            drink=user.drink[user.username],
            drink_amount=len(user.drink[user.username]['drink_name']),
            error = error
        )

    if 'change' in session :
        change = session['change']
        session.pop('change',None)
        return render_template('cashier.html', 
            username=user.username, 
            food=user.food[user.username], 
            food_amount= len(user.food[user.username]['food_name']),
            drink=user.drink[user.username],
            drink_amount=len(user.drink[user.username]['drink_name']),
            change = change
        )

    
    return render_template('cashier.html', 
        username=user.username, 
        food=user.food[user.username], 
        food_amount= len(user.food[user.username]['food_name']),
        drink=user.drink[user.username],
        drink_amount=len(user.drink[user.username]['drink_name'])
    ) 

@app.route('/invoice', methods=['GET','POST'])
def invoice() :
    if request.method == 'POST' :
        user = userService(session['username'],session['password'])
        serial_number = user.generateSerialNumber()

        # Obtain food Data
        food_name = request.form.getlist('food_name[]')
        food_price = request.form.getlist('food_price[]')
        food_unit = request.form.getlist('food_unit[]')
        food_amount = len(food_name)

        # Obtain drink Data
        drink_name = request.form.getlist('drink_name[]')
        drink_price = request.form.getlist('drink_price[]')
        drink_unit = request.form.getlist('drink_unit[]')
        drink_amount = len(drink_name)

        total = 0
        error_count = 0

        #counting Food Total Price
        for x in range(0,food_amount) :
            food_unit[x] = int(food_unit[x])
            food_price[x] = int(food_price[x])
            if food_unit[x] > 0 :
                total = total + food_unit[x] * food_price[x]
            else :
                error_count = error_count + 1

        #counting Drink Total Price
        for x in range(0,drink_amount) :
            drink_unit[x] = int(drink_unit[x])
            drink_price[x] = int(drink_price[x])
            if drink_unit[x] > 0 :
                total = total + drink_unit[x] * drink_price[x]
            else :
                error_count = error_count + 1

        if error_count == food_amount + drink_amount:
            session['error'] = 'Submit Error, you must input your food/drink amount'
            return redirect(url_for('cashier', username=session['username']))

        # Assign food data value to session variable
        session['food_name'] = food_name.copy()
        session['food_price'] = food_price.copy()
        session['food_unit'] = food_unit.copy()
        session['food_amount'] = food_amount

        # Assign drink data value to session variable
        session['drink_name'] = drink_name.copy()
        session['drink_price'] = drink_price.copy()
        session['drink_unit'] = drink_unit.copy()
        session['drink_amount'] = drink_amount
        
        # assign serial number to session variable
        session['serial_number'] = serial_number

        # assign total price value to session variable
        session['total'] = total

    return render_template('invoice.html',
        total=session['total'], 
        food_unit=session['food_unit'], 
        food_name=session['food_name'], 
        food_price=session['food_price'],
        food_amount=session['food_amount'],
        drink_unit=session['drink_unit'], 
        drink_name=session['drink_name'], 
        drink_price=session['drink_price'],
        drink_amount=session['drink_amount'],
        serial=session['serial_number']
     )

@app.route('/payment', methods=['GET','POST'])
def payment() :
    if request.method == 'POST' :
        money = int(request.form['money'])
        total = int(request.form['total'])
        
        change = money - total
        session['change'] = change
        
        session.pop('food_unit',None)
        session.pop('food_name',None)
        session.pop('food_price',None)
        session.pop('food_amount',None)

        session.pop('drink_unit',None)
        session.pop('drink_name',None)
        session.pop('drink_price',None)
        session.pop('drink_amount',None)

        session.pop('total',None)
        session.pop('serial_number',None)
        return redirect(url_for('cashier',username=session['username']))

@app.route('/cancel_payment')
def cancel_payment() :
    session.pop('food_unit',None)
    session.pop('food_name',None)
    session.pop('food_price',None)
    session.pop('food_amount',None)

    session.pop('drink_unit',None)
    session.pop('drink_name',None)
    session.pop('drink_price',None)
    session.pop('drink_amount',None)

    session.pop('total',None)
    session.pop('serial_number',None)
    return redirect(url_for('cashier',username=session['username']))      
    
@app.route('/logout')
def logout() :
    session.pop('username',None)
    session.pop('password',None)
    return redirect(url_for('index'))