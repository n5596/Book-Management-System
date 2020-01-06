from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'F9cdecd29&'
app.config['MYSQL_DB'] = 'book_management_project'

mysql = MySQL(app)
@app.route('/home')  
def home():  
    return "<html><body>" + s + "</body></html>" 

universal_user = ''
id_store = ''

@app.route('/', methods=['GET', 'POST'])
def login():
    print('here')
    if request.method == "POST" and request.form['btn'] == 'Login':
        details = request.form
        uname = details['uname']
        pw = details['pw']
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) from User where Username = (%s) and Password = (%s)", [uname, pw])
        data = cur.fetchall()  

        universal_user = uname
        print('CYCYCY',url_for('login'))

        if data == ((1,),): 
            return redirect(url_for('index', messages=universal_user))
        elif data == ((0,),):
            return render_template('login.html', data= (('Please enter the correct login information.',),))

    if request.method == "POST" and request.form['btn'] == 'Manager Login':
        details = request.form
        uname = details['uname']
        pw = details['pw']
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) from Manager where Username = (%s) and Password = (%s)", [uname, pw])
        data = cur.fetchall()  

        universal_user = uname
        print('CYCYCY',url_for('login'), data)

        if data == ((1,),): 
            cur = mysql.connection.cursor()
            cur.execute("SELECT StoreID from Manager where Username = (%s) and Password = (%s)", [uname, pw])
            d = cur.fetchall() 
            d_tuple = d[0]
            id_store = d_tuple[0]

            print(id_store)
            return redirect(url_for('manager', messages=id_store))
        elif data == ((0,),):
            return render_template('login.html', data= (('Please enter the correct login information.',),))

    if request.method == "POST" and request.form['btn'] == 'Sign Up':
        details = request.form
        uname = details['uname']
        pw = details['pw']
        name = details['name']
        genre = details['genre']

        cur = mysql.connection.cursor()
        cur.execute("SELECT Username from User")
        data = cur.fetchall()

        if (''+uname,) in data:
            return render_template('login.html', data= (('Username already taken up. Choose another username.',),))
        
        if genre == 'Fantasy' or genre == 'Mystery' or genre == 'Romance' or genre == 'Non-fiction' or genre == 'Drama':
            cur.execute("INSERT into User VALUES ((%s), (%s), (%s), (%s))", [uname, pw, name, genre])
            mysql.connection.commit()
            return render_template('login.html', data= (('Sign Up was successful. Login to proceed.',),))
        else:
            return render_template('login.html', data= (('Choose a valid genre. Valid genres include Drama, Mystery, Romance, Non-fiction and Fantasy.',),))
    return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    universal_user = request.args['messages']

    data = ''
#2
    if request.method == "POST" and request.form['btn'] == 'Find Books by Author':
        print('find books by author')
        details = request.form
        a_name = details['author_name']

        if a_name == '':
            return render_template('index.html', data=(('Please provide the necessary information.',),))
        cur = mysql.connection.cursor()
        cur.execute("SELECT Title from Books where Author = (%s)", [a_name])
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', data=data)
#3
    if request.method == "POST" and request.form['btn'] == 'Find Books by Genre':
        print('find books by genre')
        details = request.form
        g_name = details['genre_name']

        if g_name == '':
            return render_template('index.html', data=(('Please provide the necessary information.',),))
        cur = mysql.connection.cursor()
        cur.execute("SELECT Title from Books where Genre = (%s)", [g_name])
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', data=data)
#4
    if request.method == "POST" and request.form['btn'] == 'Add a Book to your Read Bookshelf':
        print('add book')
        details = request.form
        b_name = details['book_name']
        rating = details['rating']

        if b_name == '' or rating == '':
            return render_template('index.html', data=(('Please provide the necessary information.',),))

        if int(rating) > 0 and int(rating) <6:
            cur = mysql.connection.cursor()
            cur.execute("select ISBN_Code, Author from Books where Title = (%s)", [b_name])
            data = cur.fetchall()   

            d_tuple = data[0]
            isbn_code = d_tuple[0]
            author = d_tuple[1]

            cur.execute("INSERT into Books_Read VALUES ((%s), (%s), (%s), (%s))", [universal_user, isbn_code, rating, author])
            mysql.connection.commit()
            cur.close()
            return render_template('index.html', data= (('Book added to bookshelf.',),))
        else:
            return render_template('index.html', data= (('The rating should be between 1 and 5 (inclusive).',),))

#Bonus
    if request.method == "POST" and request.form['btn'] == 'Find Books Read by User':
        print('find books read by user')
        #details = request.form
        #u_name = details['user_name']

        cur = mysql.connection.cursor()
        cur.execute("select Title from Books where ISBN_Code in (select ISBN_Code from Books_Read where username = (%s))", [universal_user])
        data = cur.fetchall()
        print(data)

        cur.close()
        return render_template('index.html', data=data)

#5
    if request.method == "POST" and request.form['btn'] == 'Find highest rated book of author':
        print('find highest rated book')
        details = request.form
        a_name = details['author_name']

        if a_name == '':
            return render_template('index.html', data=(('Please provide the necessary information.',),))
        cur = mysql.connection.cursor()
        cur.execute("select ISBN_Code from (select ISBN_Code, avg(rating) as avg_rating from Books_Read where Author = ((%s)) group by ISBN_Code order by avg_rating desc) as X limit 0, 1", [a_name])
        data = cur.fetchall()
        d_tuple = data[0]
        code = d_tuple[0]
        #print(code)

        cur.execute("select Title from Books where ISBN_Code = ((%s))", [code]) 
        data = cur.fetchall()       
        #print(data)
        cur.close()
        return render_template('index.html', data=data)

#6
    if request.method == "POST" and request.form['btn'] == 'Recommend book':
        print('recommend book')
        cur = mysql.connection.cursor()
        cur.execute("select count(*) from Books_Read where Username = ((%s))", [universal_user])
        data = cur.fetchall()
        d_tuple = data[0]
        num = d_tuple[0]
        if num > 0:
            cur.execute("select Genre,count(*) as counting from Books where ISBN_Code in (select ISBN_Code from Books_Read where Username = ((%s))) group by Genre order by counting desc limit 0,1", [universal_user])         
            data = cur.fetchall()
            d_tuple = data[0]
            fave_genre = d_tuple[0] 
        else:            
            cur.execute("select Favorite_genre from User where Username = ((%s))", [universal_user]) 
            data = cur.fetchall()
            d_tuple = data[0]
            fave_genre = d_tuple[0] 

        cur.execute("select Title,avg(rating) as avg_rating from Books_Read inner join Books on Books.ISBN_Code = Books_Read.ISBN_Code where Genre = ((%s)) group by Books.ISBN_Code order by avg_rating desc limit 0,1", [fave_genre])      
        data = cur.fetchall()    
        d_tuple = data[0]
        rec = d_tuple[0] 
        #print('RECOMMENEDED', rec)
        cur.close()
        return render_template('index.html', data=((rec,),))

#7
    if request.method == "POST" and request.form['btn'] == 'Find Bookstores Which Carry a Specific Book':
        print('find bookstores wrong')
        details = request.form
        u_name = details['store_name']

        if u_name == '':
            return render_template('index.html', data=(('Please provide the necessary information.',),))
        cur = mysql.connection.cursor()
        cur.execute("select Name, Address from Bookstore cross join Book_Selling where Bookstore.StoreID = Book_Selling.StoreID and ISBN_Code in (select ISBN_Code from Books where Title = (%s))", [u_name])
        data = cur.fetchall()

        cur.close()
        #print('ATTENTION',data)
        return render_template('index.html', data=data)

#8
    if request.method == "POST" and request.form['btn'] == 'Find the Most Critically-Acclaimed Book':
        print('find critically acclaimed book')
        cur = mysql.connection.cursor()
        cur.execute("select a.ISBN_Code, (c1+c2) as acclaim from (select ISBN_Code,sum(Number_of_Copies_Sold) as c1 from Book_Selling group by ISBN_Code) as a join (select ISBN_Code,count(Username) as c2 from Books_Read where Rating = 5 group by ISBN_Code) as b on a.ISBN_Code = b.ISBN_Code order by acclaim desc limit 0,1")
        data = cur.fetchall()
        d_tuple = data[0]
        code = d_tuple[0] 
        cur.execute("select Title from Books where ISBN_Code = ((%s))", [code])
        data = cur.fetchall()        
        
        cur.close()
        #print('ATTENTION',data)
        return render_template('index.html', data=data)


#9
    if request.method == "POST" and request.form['btn'] == 'Find Books Ordered by User':
        print('find books ordered by user')
        #details = request.form
        #u_name = details['user_name']

        cur = mysql.connection.cursor()
        cur.execute("select Title from Books where ISBN_Code in (select ISBN_Code from Orders where username = (%s))", [universal_user])
        data = cur.fetchall()
        print(data)

        cur.close()
        return render_template('index.html', data=data)

#10
    if request.method == "POST" and request.form['btn'] == 'Find Books Written by Authors Who Have Won a Specific Award':
        print('find books award')
        details = request.form
        a_name = details['award_name']

        if a_name == '':
            return render_template('index.html', data=(('Please provide the necessary information.',),))
        cur = mysql.connection.cursor()
        #print(a_name)
        if a_name == 'Hugo Award':
            cur.execute("select Title, Author from Books where Author in (select Name from Author where Hugo_Award=\"Yes\")")
        elif a_name == 'Man Booker Prize':
            cur.execute("select Title from Books where Author in (select Name from Author where Man_Booker_Prize=\"Yes\")")
        elif a_name == 'Pulitzer Prize':
            cur.execute("select Title from Books where Author in (select Name from Author where Pulitzer_Prize=\"Yes\")")
        data = cur.fetchall()
        #print('FOUND',data)
        cur.close()
        #print('ATTENTION',data)
        return render_template('index.html', data=data)

#11
    if request.method == "POST" and request.form['btn'] == 'Find Book with Maximum Orders':
        print('find book with max orders')
        cur = mysql.connection.cursor()
        cur.execute("select Title from Books inner join (select ISBN_Code as code, count(*) as ord from Orders group by ISBN_Code) as v on Books.ISBN_Code = v.code order by ord desc limit 1")
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', data=data)

#13
    if request.method == "POST" and request.form['btn'] == 'Find Bookstores Which Carry a Book':
        details = request.form
        title = details['title']
        if title == '':
            return render_template('index.html', data=(('Please provide the necessary information.',),))

        cur = mysql.connection.cursor()
        cur.execute("select StoreID, Name from Bookstore where StoreID in (select distinct StoreID from Book_Selling where ISBN_Code in (select ISBN_Code from Books where Title=((%s))))", [title])
        data = cur.fetchall()

        cur.close()
        return render_template('index.html', data=data)

#14
    if request.method == "POST" and request.form['btn'] == 'Order a Book':
        print('order book')
        details = request.form
     
        title = details['title']
        copies = details['copies']
        storeid = details['storeid']
        if title == '' or copies == '' or storeid == '':
            return render_template('index.html', data=(('Please provide the necessary information.',),))
        cur = mysql.connection.cursor()
        cur.execute("select max(OrderID) from Orders")
        data = cur.fetchall()
        data_tuple = data[0]
        prev = data_tuple[0]

        cur.execute("select ISBN_Code, Price from Books where Title = ((%s))", [title])
        data = cur.fetchall()
        data_tuple = data[0]
        code = data_tuple[0]
        price = data_tuple[1]
        amount = float(price)*float(copies)
        print('info', prev+1, universal_user, storeid, code, copies, price, amount)
        
        cur.execute("INSERT into Orders values ((%s), (%s), (%s), (%s), (%s), (%s))", [prev+1, universal_user, storeid, code, copies, amount])   
        mysql.connection.commit()     
        
        cur.close()
        return render_template('index.html', data=(('The order was successful.',),))
#15
    if request.method == "POST" and request.form['btn'] == 'Logout':
        print('get out')
        return redirect('/')  

    return render_template('index.html', data=data)


@app.route('/manager', methods=['GET', 'POST'])
def manager():
    print('i have entered this')
    id_store = request.args['messages']
    data = ''

    if request.method == "POST" and request.form['btn'] == 'Find Books Ordered by User':
        print('find books ordered by user')
        details = request.form
        u_name = details['user_name']

        cur = mysql.connection.cursor()
        cur.execute("select Title from Books where ISBN_Code in (select ISBN_Code from Orders where StoreID=((%s)) and username = ((%s)))", [id_store, u_name])
        data = cur.fetchall()

        cur.close()
        return render_template('manager.html', data=data)

    if request.method == "POST" and request.form['btn'] == 'Find Orders Made to the Bookstore':
        cur = mysql.connection.cursor()
        cur.execute("select OrderID, Username,Title,Amount, Orders.Price from Orders join Books on Orders.ISBN_Code = Books.ISBN_Code where StoreID=((%s)) ", [id_store])
        data = cur.fetchall()        
        cur.close()

        a_data = ('OrderID','Username','Title','Amount','Price')
        b_data = (a_data,)+data
        return render_template('manager.html', data=b_data)

    if request.method == "POST" and request.form['btn'] == 'See Pending Orders':
        cur = mysql.connection.cursor()
        cur.execute("select SupplyID, Title, Copies, Amount from Inventory join Books on Inventory.ISBN_Code=Books.ISBN_Code where StoreID=((%s))", [id_store])
        data = cur.fetchall()        
        cur.close()
        a_data = ('SupplyID', 'Title', 'Number of Copies', 'Amount')
        b_data = (a_data,)+data
        return render_template('manager.html', data=b_data)

    if request.method == "POST" and request.form['btn'] == 'Approve Pending Orders':
        details = request.form
        idd = details['id']

        cur = mysql.connection.cursor()
        cur.execute("delete from Inventory where SupplyID=((%s))", [idd])
        mysql.connection.commit()     
        cur.close()
        return render_template('manager.html', data=(('The order was approved.',),))

    if request.method == "POST" and request.form['btn'] == 'Logout':
        print('get out')
        return redirect('/') 
    return render_template('manager.html', data=data)
if __name__ == '__main__':
    app.run()
