import mysql.connector as mysql
import random
import string

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "F9cdecd29&",
    database = "book_management_project"
)

cursor = db.cursor()

#-----------CREATING TABLES--------------
query = "CREATE TABLE Author(Name varchar(80), Hugo_Award varchar(80), Man_Booker_Prize varchar(80), Pulitzer_Prize varchar(90))"
cursor.execute(query)
db.commit()

query = "CREATE TABLE Book_Selling(StoreID int, ISBN_Code varchar(40), Number_of_Copies_Available int, Number_of_Copies_Sold int)"
cursor.execute(query)
db.commit()

query = "CREATE TABLE Books(ISBN_Code varchar(20), Title varchar(200), Genre varchar(50), Price float, Author varchar(50), PRIMARY KEY(ISBN_Code))"
cursor.execute(query)
db.commit()

query = "CREATE TABLE Books_Read(Username varchar(50), ISBN_Code varchar(20), Rating int, Author varchar(60))"
cursor.execute(query)
db.commit()

query = "CREATE TABLE Bookstore(StoreID int, Name varchar(50), Address varchar(100), PRIMARY KEY(StoreID))"
cursor.execute(query)
db.commit()

query = "CREATE TABLE Inventory(SupplyID int, StoreID int, ISBN_Code varchar(20), Copies int, Amount float, PRIMARY KEY(SupplyID))"
cursor.execute(query)
db.commit()

query = "CREATE TABLE Manager(Username varchar(50), Name varchar(50), Password varchar(50), StoreID int, PRIMARY KEY(Username))"
cursor.execute(query)
db.commit()

query = "CREATE TABLE Orders(OrderID int, Username varchar(60), StoreID int, ISBN_Code varchar(20), Amount int, Price float, PRIMARY KEY(OrderID))"
cursor.execute(query)
db.commit()

query = "CREATE TABLE User(Username varchar(70), Password varchar(60), Name varchar(50), Favorite_genre varchar(40), PRIMARY KEY(Username))"
cursor.execute(query)
db.commit()

#-----------GENERATING DATA FOR THE USER TABLE------------------
username =['copperfieldstudied','brokelincoln','skyrocketberkshire','bottomryscadgers','palacememory','rayblandness','chefiguana','recentmarton', 'braggglass','bodychokehold','penaltylitmus','acidmarina','judgmentavocet','soupdoctor','affiliatestift','severitytruth','wanderstrunch',
'flushedordered','abbywoodchuck','flashfeatures','ohmalloy','baggyperjurer','rumblerunny','tauntlenville','giveawaycapillary','excusebackwash',
'burlyoxford','bootlesspolicy','maybeundertook','karmachoice','frostilygodwit']

passwords = []

names = ['Karren Forti', 'Brigid Ragsdale', 'Marybelle Montalvan', 'Francesca Stockbridge','Mohammad Benninger','Anglea Coate','Leann Frechette','Janey Mondor','Leif Bjelland','Joannie Moreno','Ida Sorber','Mamie Marlow','Margeret Normand','Douglass Muriel','Xavier Hatt','Gregorio Pelkey','Norbert Runkle','Giuseppina Batchelder','Margene Rochelle','Alysia Sever','Efrain Hibbitts','Alysa Gorman','Princess Womble','Katina Stoneking','Carman Goodspeed','Lina Baze','Vanetta Bone','Charis Mohamed','Tasia Mccann','Izetta Gamez','Tynisha Hocutt','Nancy Roussell']

genre = ['Mystery', 'Fantasy', 'Drama', 'Romance', 'Non-fiction']

user_values = []
for name in username:
    pw = randomString(8)
    
    j = len(names)
    name_ind = random.randint(0, j-1)
    k = len(genre)
    genre_ind = random.randint(0, k-1)
    val = (name, pw, names[name_ind], genre[genre_ind])
    user_values.append(val)

query = "INSERT INTO User VALUES (%s, %s, %s, %s)"

cursor.executemany(query, user_values)
db.commit()

#----------GENERATING DATA FROM BOOKS TABLE--------------------
book_info = [[''+randomString(5), 'Animal Farm', 'George Orwell', 'Drama'], [''+randomString(5),'Pride and Prejudice', 'Jane Austen','Romance'], [''+randomString(5),'The Book Thief', 'Markus Zusak', 'Drama'], [''+randomString(5),'The Picture of Dorian Gray', 'Oscar Wilde', 'Drama'], [''+randomString(5),'Jane Eyre', 'Charlotte Bronte', 'Romance'], [''+randomString(5),'The Alchemist', 'Paolo Coelho', 'Fantasy'], [''+randomString(5),'Of Mice and Men', 'John Steinbeck', 'Drama'], [''+randomString(5),'Brave New World','Aldous Huxley', 'Fantasy'], [''+randomString(5),'The Catcher in the Rye', 'J. D. Salinger', 'Drama'], [''+randomString(5),'Fahrenheit 451', 'Ray Bradbury', 'Fantasy'], [''+randomString(5),'Harry Potter and the Sorcerers Stone', 'J. K. Rowling', 'Fantasy'], [''+randomString(5),'The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy'], [''+randomString(5),'A Game of Thrones', 'George R. R. Martin', 'Fantasy'], [''+randomString(5),'The Chronicles of Narnia', 'C.S. Lewis', 'Fantasy'], [''+randomString(5),'Freakonomics: A Rogue Economist Explores the Hidden Side of Everything','Steven D. Levitt', 'Non-fiction'], [''+randomString(5),'A Short History of Nearly Everything','Bill Bryson', 'Non-fiction'], [''+randomString(5),'Guns, Germs, and Steel: The Fates of Human Societies', 'Jared Diamond', 'Non-fiction'], [''+randomString(5),'Outliers: The Story of Success', 'Malcolm Gladwell', 'Non-fiction'], [''+randomString(5),'The Tipping Point: How Little Things Can Make a Big Difference', 'Malcolm Gladwell', 'Non-fiction'], [''+randomString(5),' Blink: The Power of Thinking Without Thinking','Malcolm Gladwell', 'Non-fiction'], [''+randomString(5),'Persuasion', 'Jane Austen', 'Romance'], [''+randomString(5),'Sense and Sensibility','Jane Austen','Romance'],[''+randomString(5),'And Then There Were None', 'Agatha Christie','Mystery'], [''+randomString(5),'Rebecca', 'Daphne du Maurier','Mystery'], [''+randomString(5),'The Name of the Rose', 'Umberto Eco','Mystery'], [''+randomString(5),'The Shadow of the Wind', 'Carlos Ruiz Zafon', 'Mystery'], [''+randomString(5),'The Mysterious Affair at Styles', 'Agatha Christie', 'Mystery'], [''+randomString(5),'1984', 'George Orwell', 'Drama'], [''+randomString(5),'East of Eden', 'John Steinbeck', 'Drama'], [''+randomString(5),'The Grapes of Wrath', 'John Steinbeck', 'Drama'], [''+randomString(5),'Harry Potter and the Goblet of Fire', 'J. K. Rowling', 'Fantasy'], [''+randomString(5),'Harry Potter and the Chamber of Secrets', 'J. K. Rowling', 'Fantasy'], [''+randomString(5),'At Home: A Short History of Private Life', 'Bill Bryson', 'Non-fiction'], [''+randomString(5),'My Cousin Rachel', 'Daphne du Maurier', 'Mystery'], [''+randomString(5),'To Kill a Mockingbird', 'Harper Lee', 'Drama'], [''+randomString(5),'The Hobbit, or There and Back Again', 'J.R.R. Tolkien', 'Fantasy'], [''+randomString(5),' The Fellowship of the Ring', 'J.R.R. Tolkien', 'Fantasy'], [''+randomString(5),'The Old Man and the Sea', 'Ernest Hemingway', 'Drama'], [''+randomString(5),'The Return of the King', 'J.R.R. Tolkien', 'Fantasy'], [''+randomString(5),'Angels and Demons', 'Dan Brown', 'Mystery'], [''+randomString(5),'Gone Girl', 'Gillian Flynn', 'Mystery'], [''+randomString(5),'The Woman in White', 'Wilkie Collins', 'Mystery'], [''+randomString(5),'A Study in Scarlet', 'Arthur Conan Doyle', 'Mystery'], [''+randomString(5),'The Hounds of Baskervilles', 'Arthur Conan Doyle', 'Mystery'], [''+randomString(5), 'The Blind Assassin', 'Margaret Atwood', 'Drama'], [''+randomString(5), 'The Handmaids Tale', 'Margaret Atwood', 'Drama'], [''+randomString(5), 'Lord of the Flies', 'William Golding', 'Drama'], [''+randomString(5), 'The Inheritors', 'William Golding', 'Drama'], [''+randomString(5), 'Anna Karenina', 'Leo Tolstoy', 'Romance'], [''+randomString(5), 'The Thornbirds', 'Colleen McCullough', 'Romance'], [''+randomString(5), 'War and Peace', 'Leo Tolstoy', 'Drama']]

book_values = []
for x in book_info:
    price = random.randint(1, 30)
    val = (x[0], x[1],x[3], price, x[2])
    book_values.append(val)

query = "INSERT INTO Books VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(query, book_values)
db.commit()


#------------GENERATING BOOKS READ-----------------------
books_read = []
entries = 0
while entries <= 600:
    m = len(username)
    n = len(book_info)
    i = random.randint(0, m-1)
    j = random.randint(0, n-1)
    entries = entries+1
    x = book_info[j]
    rating = random.randint(1, 5)
    val = (username[i], x[0], rating, x[2])
    books_read.append(val)

query = "INSERT INTO Books_Read VALUES (%s, %s, %s, %s)"
cursor.executemany(query, books_read)
db.commit()

#----------AUTHOR-----------------------------
hugo = ['George Orwell', 'Oscar Wilde', 'Ray Bradbury', 'J. K. Rowling', 'J.R.R. Tolkien', 'George R. R. Martin']
pulitzer = ['John Steinbeck', 'Ray Bradbury', 'Jared Diamond', 'Harper Lee', 'Ernest Hemingway']
booker = ['William Golding', 'Margaret Atwood']

all_authors = [x[2] for x in book_info]
all_authors = list(set(all_authors))

author_info = []
for a in all_authors:
    a1 = "No"
    a2 = "No"
    a3 = "No"
    if a in hugo:
        a1 = "Yes"
    if a in booker:
        a2 = "Yes"
    if a in pulitzer:
        a3 = "Yes"
    val = (a, a1, a2, a3)
    author_info.append(val)

query = "INSERT INTO Author VALUES (%s, %s, %s, %s)"
cursor.executemany(query, author_info)
db.commit()

#--------BOOKSTORE--------------------------
bookstores = [('Barnes & Nobles', '850 Hawthorne Drive GA'), ('Subtext', '573 Naseby Cliff CA'), ('Lending Library', '683 Walnut Knoll Drive WI'), ('A New Chapter', '236 Badger Point NY'), ('Books-R-Us', '746 Severn Moorings RI'), ('The Book Train', '992 Wenger Crescent St CA'), ('Bookland', '123 Hudleston Road WI'), ('Author Attic', '653 Morris Path AL'), ('Barnes & Nobles', '443 Greenland Town AZ'), ('Book Smart', '934 Morris Path IL'), ('Crosswords', '452 Coltsfoot Fields MN'), ('Crosswords', '543  Salway Road ME'), ('Barnes & Nobles', '654 Stoneyhurst Drive NV'), ('Crosswords', '528 Somerville Hall NJ'), ('Subtext', '823 Stockheath Lane NY'), ('Lending Library', '643 Birch Square NC'), ('The Book Train', '692 Swan Corner MD'), ('The Book Train' '148 Sefton Circle GA'), ('Author Attic', '432 Well Cedars CA')]

store_info = []
count = 1
for a in bookstores:
    val = (count, a[0], a[1])
    store_info.append(val)
    count = count+1

query = "INSERT INTO Bookstore VALUES (%s, %s, %s)"
cursor.executemany(query, store_info)
db.commit()

#------ORDERS---------------------------
orders_info = []
for i in range(400):
    j = len(username)
    v1 = random.randint(0, j-1)
    k = len(bookstores)
    v2 = random.randint(0, k-1)
    l = len(book_info)
    v3 = random.randint(0, l-1)
    vv = book_info[v3]
    v4 = random.randint(0, 20) #amount
    val = (i, username[v1], v2, vv[0], v4, 0)
    orders_info.append(val)

query = "INSERT INTO Orders VALUES (%s, %s, %s, %s, %s, %s)"
cursor.executemany(query, orders_info)
db.commit()

#------BOOKSELLING---------------------------
bookselling_info = []
for i in range(800):
    k = len(bookstores)
    v2 = random.randint(0, k-1)
    l = len(book_info)
    v3 = random.randint(0, l-1)
    vv = book_info[v3]

    k1 = random.randint(0, 50)
    k2 = random.randint(0,200)
    val = (v2, vv[0], k1, k2)
    bookselling_info.append(val)

query = "INSERT INTO Book_Selling VALUES (%s, %s, %s, %s)"
cursor.executemany(query, bookselling_info)
db.commit()

#-------INVENTORY------------------
inventory_info = []
for i in range(400):
    k = len(bookstores)
    v2 = random.randint(0, k-1)
    l = len(book_info)
    v3 = random.randint(0, l-1)
    vv = book_info[v3]
    gbg = random.randint(0,50)
    val = (i, v2, vv[0], gbg, 0)
    inventory_info.append(val)

query = "INSERT INTO Inventory VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(query, inventory_info)
db.commit()

#------MANAGER---------------
manager_info = [('m001','Johnie Wiles', 'fwrgior',1), ('m002', 'Adena Priestley', 'nsgwepr32',2), ('m003','Kasandra Asuncion', 'anfo32rewm', 3), ('m004', 'Tera Daubert', '23940rwd',4), ('m005','Le Westergard', '4389wnw',5), ('m006','Zona Defibaugh', 'efqi32',6), ('m007','Petra Wohlgemuth','34nrieo34',7),('m008','Norris Grey','miow54',8),('m009', 'Izetta Montiel', 'mfweio32',9), ('m010', 'Cecelia Revell', 'nfewio54',10), ('m011', 'Woodrow Ridenour', 'mgi367',11), ('m012', 'Lea Antoine','mwer',12),('m013','Leonard Sthilaire','043t4pg',13), ('m014','Rae Effler', 'fwio',14), ('m015','Sun Mcadoo', 'moewp',15), ('m016', 'Tim Rossetti', 'mfiwo320ri',16), ('m017', 'Long Saez', 'moppper',17), ('m018','Nita Chabolla','mighy',18), ('m019', 'Corrina Hinds','fniewro32',19), ('m020', 'Mireille Canup','mfiweop',18), ('m021', 'Tami Casperson', 'jf3490', 4), ('m022','Charlette Capshaw', 'pweofwe',1), ('m023','Adaline Roland', 'kfwe0p3',5), ('m024', 'Alita Figgs','p2o13',7), ('m025', 'Ethel Line','mferger',9), ('m026','Wan Mccluney', 'rewiqp',3), ('m027','Cathleen Bolles', '12940m', 10), ('m028', 'Dolores Mrozek', 'wepo',2), ('m029', 'Geri Baumgardner', 'fwemio',15), ('m030', 'Craig Reiber', 'wqei', 13)]

query = "INSERT INTO Manager VALUES (%s, %s, %s, %s)"
cursor.executemany(query, manager_info)
db.commit()
    
#----------UPDATING TABLES---------------
query = "update Orders O, Books B set O.Price = O.Amount*B.Price where O.ISBN_Code = B.ISBN_Code"
cursor.execute(query)
db.commit()

query = "update Book_Selling B, (select ISBN_Code, count(*) as cc from Orders group by ISBN_Code) as t2 set B.Number_of_Copies_Sold=t2.cc where B.ISBN_Code = t2.ISBN_Code"
cursor.execute(query)
db.commit()


query = "update Inventory I, Books B set I.Amount=I.copies*B.Price where I.ISBN_Code = B.ISBN_Code"
cursor.execute(query)
db.commit()

