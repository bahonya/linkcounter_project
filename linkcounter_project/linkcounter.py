from linkcounter_project.csv_logging import CSV_Logging
from linkcounter_project.parser import Parser
from linkcounter_project.db import Database
from sys import argv
from os.path import dirname, abspath, join




wiki_random = 'https://en.wikipedia.org/wiki/Special:Random'
path_to_db = join(dirname(dirname(abspath(__file__))),'databasename.sqlite3')

class Linkcounter:
    def __init__(self):
        self.Parser = Parser(wiki_random)
        self.CSV_Logging = CSV_Logging()
        self.Database = Database(path_to_db)
        self.Database.create_wiki_tables()

    def message_to_print(self, list):
        message = f"""
        Wiki Page Title - {list[0]}
        Link to this article - {list[1]}
        Number of links on this page - {list[2]}
        Linkcounter parsed this article at {list[3]} 
        List of links:
        {list[4]}
        """
        return message
    
    def help_message(self):
        print(f"""
        List of terminal commands:

        python3 linkcounter.py --get random
        Use this command to jump to the random wiki page. Get number of links and list of links on that page

        python3 linkcounter.py --view 'article_name'
        Use this command to get number of links and list of links by given article name if it was already parsed

        python3 linkcounter.py --count 'article_name'
        Use this command to get number of links by given article name if it was already parsed

        python3 linkcounter.py --help
        """)
        
    def get_random_links(self):
        """
        linkcounter.py --get random
        Discover random wiki page, look for links
        """
        print("Parsing random wiki page")
        random_data = self.Parser.get_output()
        self.CSV_Logging.run(random_data)
        #Check if entry already exists in db, else insert it in
        with self.Database as db:
            if db.find_entry_by_title(random_data[0]) is None:
                db.insert_data(random_data)
                print(f"New entry was added to the database, wiki page title - {random_data[0]}")
                print(self.message_to_print(random_data))
                return self.message_to_print(random_data)
            else:
                print("This entry already exists in database")
                print(self.message_to_print(random_data))
                return self.message_to_print(random_data)

    def view_article(self, article):
        """
        linkcounter.py --view 'article_name'
        Look if article with given title was already parsed
        """
        print("Looking for given article name in db")
        with self.Database as db:
            entry = db.find_entry_by_title_full_info(article)
            if entry is None:
                print("No etries were found in database by given article name")
                return "No etries were found in database by given article name"
            else:
                list_to_print = list(entry[0])
                #We remove element with index before because its an extra article name
                del list_to_print[4]
                print(self.message_to_print(list_to_print))
                return self.message_to_print(list_to_print)

    def show_number_of_links_by_article_name(self, article):
        """
        linkcounter.py --count 'article_name'
        Return number of links on page with given article name
        """
        print("Looking for given article name in db")
        with self.Database as db:
            entry = db.find_entry_by_title(article)
            if entry is None:
                print("No etries were found in database by given article name")
                return "No etries were found in database by given article name"
            else:
                list_to_print = list(entry[0])
                message_to_print = f"""
                Article '{list_to_print[0]}' has {list_to_print[2]} links.
                Data was parsed {list_to_print[3]}
                """
                print(message_to_print)
                return message_to_print

    def show_list_of_links_by_article_name(self, article):
        """
        Function is called from GUI
        Return only list of links in bage by given title
        """
        with self.Database as db:
            entry = db.find_entry_by_title_second_table(article)
            if entry is None:
                return "No etries were found in database by given article name"
            else:
                list_to_print = list(entry[0])
                return list_to_print[1]


def main():
    """
    main function, that is called from the console
    depending on arguments it calls other methods"""
    session = Linkcounter()
    try:
        if (argv[1] == '--get') and (argv[2] == 'random'):
            session.get_random_links()
        elif argv[1] == '--view':
            session.view_article(argv[2])
        elif argv[1] == '--count':
            session.show_number_of_links_by_article_name(argv[2])
        elif argv[1] == '--help':
            session.help_message()
        else:
            session.help_message()
    except:
        session.help_message()