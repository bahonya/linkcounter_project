Task for RPA position in EPAM

1)clone repository
2)pip3 install -e .
3)linkcounter --help or linkcounter_gui

Create an application to count the number of links in the page. Use a wiki random page https://en.wikipedia.org/wiki/Special:Random. This application has to:
	1. get a list of all links (a href) in the random page.
	2. save logs of processed articles in the CSV file.
	3. save records of processed articles in the database (DB).
	4. get the number of links.
	
Implement console and GUI version of the application.
In case of a console, use these commands:
	Example of console commands:
		get list of links:
			linkcounter --get random
		
		get saved data from DB tables (by article name):
			linkcounter --view article_name
			
		get count of links for article (by article name):
			linkcounter --count article_name

GUI implementation (you can use Tkinter module or any other):
		a field for a random link at the top of the window and button 'Get a list of links'
		a field for article name and button 'Get saved links' and button 'Count'
		
		output:
			field with article name, links

Logs of processed articles has to be added to the CSV file. File format:
	date time name of article
	
List with links has to be saved in the database tables (use sqlite). Articles have to be unique, do not save if the article already exists.

Implement project by using OOP.

Optional: 
	implement unit tests.
	implement logging.
	
!!!
setup.py file has to be included in the application to build into package with command sdist or install by pip.