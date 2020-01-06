#--------READ ME-----------

To initialize:
1. In the generate_data.py file, modify the host, user and passwd variables to the appropriate values (lines 10-13). Add the host, user and password of your MySQL account.
2. In the app.py file, modify the host, user and password variables to the appropriate values (lines 6-9).

To set up the database:
1. Login to MySQL and create a database named book_management_project by using the command
		create database if not exists book_management_project;
2. Run the generate_data.py file by using the command on terminal
		python generate_data.py

To use the application:
1. Run the command on terminal:
		python app.py runserver -d
2. The terminal shows a message: "Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)". Right click on the url and
click on the "Open Link" option.
3. The application opens up on a web browser (Mozilla Firefox in my case). 
4. 

To Login as user or manager:
1. Enter the correct user credentials in the appropriate form. Since data generated is random, one can look up the User table for credentials.
	Valid credentials for the manager table are : Username: m012, Password: mwer

To Sign Up:
1. Create a profile by providing the necessary information. The valid genres are :
	genre = ['Mystery', 'Fantasy', 'Drama', 'Romance', 'Non-fiction']. No quotations needed.	
2. Login using the credentials of the newly created account.


3. User Main Page:
1. To find books by author, specify the author's name (such as "Oscar Wilde" or "Jane Austen"- no quotes needed) in the dialog box.

2. To find books by genre, specify the genre. Use only the ones shown below.
	genre = ['Mystery', 'Fantasy', 'Drama', 'Romance', 'Non-fiction']	

3. To add book to your Read bookshelf, specify the book title (such as "Rebecca" or "Persuasion") and a rating (integer 1-5, inclusive of both)

4. Press the respective buttons for the functionalities: 
	Find Books Read by User ,  Recommend book ,  Find the Most Critically-Acclaimed Book , Find Books Ordered by User,  Find Book with Maximum Orders 
 
5. To find highest rated book of author, specify the author's name (such as "Oscar Wilde")
6. To find books written by authors who have won a specific award, use either of the 3 awards:
	'Hugo Award', 'Man Booker Prize', 'Pulitzer Prize'. (No quotes needed)

7. To find bookstores which carry a book, specify the book title. The output is a storeID.
8. To order a book from a bookstore, specify the book title, number of copies (an integer) and the storeID (which is the output of the previous functionality).
9. Click on Logout button to logout.

4. Manager Main Page:
1. To find books ordered by a user from the bookstore at which the manager works, specify the username in the input box.
2. Click on the button " Find Orders Made to the Bookstore " to find all orders made by users to the bookstore.
3. Click on the button " See Pending Orders " to see all pending orders made by store employees to the inventory.
4. To approve a pending order, specify a supplyID for the " Approve Pending Orders " form. The supplyID can be found from the functionality "See Pending Orders".
5. To logout, click on the logout button.
