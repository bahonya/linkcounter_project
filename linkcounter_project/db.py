import sqlite3

class Database:
    def __init__(self, location):
        """Initialize db class variables"""
        self.__DB_LOCATION = location
        self.connection = sqlite3.connect(self.__DB_LOCATION)
        self.cursor = self.connection.cursor()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def commit(self):
        """commit changes to database"""
        self.connection.commit()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def create_table(self, create_table_sql):
        """create a database table"""
        self.cursor.execute(create_table_sql)

    def create_wiki_tables(self):
        """Creates tables for current project if they dont exist"""
        sql_create_wiki_links_count_table = """CREATE TABLE IF NOT EXISTS links_count (
                                    wiki_page_title text PRIMARY KEY,
                                    wiki_page_url text,
                                    wiki_links_count integer,
                                    timestamp text
                                ); """
        sql_create_wiki_links_list_table = """CREATE TABLE IF NOT EXISTS links_list (
                                        wiki_page_title text PRIMARY KEY,
                                        wiki_links_list
                                    );"""
        self.cursor.execute(sql_create_wiki_links_count_table)
        self.cursor.execute(sql_create_wiki_links_list_table)

    def insert_data(self, wiki_data):
        """Insert data from response to both table"""
        self.cursor.execute("""INSERT INTO links_count VALUES (?,?,?,?)""", (wiki_data[0], wiki_data[1], wiki_data[2], wiki_data[3]))
        self.cursor.execute("""INSERT INTO links_list VALUES (?,?)""", (wiki_data[0], ', '.join(wiki_data[4])))

    def find_entry_by_title(self, title):
        """Look for entry in db with given title(PRIMARY KEY)"""
        self.cursor.execute("""SELECT * FROM links_count WHERE wiki_page_title=?""", (title,))
        data=self.cursor.fetchall()
        if len(data)==0:
            return None
        else:
            return data
    
    def find_entry_by_title_full_info(self, title):
        """Look for entry in db with given title(PRIMARY KEY), inner join to give full information"""
        self.cursor.execute("""SELECT * FROM links_count 
                            INNER JOIN links_list on links_count.wiki_page_title = links_list.wiki_page_title
                            WHERE links_count.wiki_page_title=?""", (title,))
        data=self.cursor.fetchall()
        if len(data)==0:
            return None
        else:
            return data

    def find_entry_by_title_second_table(self, title):
        """Look for entry in db with given title(PRIMARY KEY) at second table. Need for GUI"""
        self.cursor.execute("""SELECT * FROM links_list WHERE wiki_page_title=?""", (title,))
        data=self.cursor.fetchall()
        if len(data)==0:
            return None
        else:
            return data


"""dbdb = Database()
test_data = ['Ramiro Fumazoni - Wikipedia',
            'https://en.wikipedia.org/wiki/Ramiro_Fumazoni',
            50,
['#mw-head', '#searchInput', '/wiki/Buenos_Aires,_Argentina', '#cite_note-1', '#cite_note-univision-2', '/wiki/Buenos_Aires,_Argentina', '#cite_note-univision-2', '#Filmography', '#Film', '#Television_roles', '#References', '#External_links', '/w/index.php?title=Ramiro_Fumazoni&action=edit&section=1', '/w/index.php?title=Ramiro_Fumazoni&action=edit&section=2', 'https://www.imdb.com/title/tt2376336/', '/w/index.php?title=Ramiro_Fumazoni&action=edit&section=3', '/wiki/Vu%C3%A9lveme_a_querer_(telenovela)', '/wiki/Charlie%27s_Angels_(2011_TV_series)', '/wiki/Angels_in_Chains', '/wiki/Grachi', 'https://es.wikipedia.org/wiki/La_ruta_blanca', '/wiki/Solamente_vos', '/wiki/Vivir_a_destiempo', '/wiki/UEPA!_Un_escenario_para_amar', 'https://www.imdb.com/title/tt4941556/', '/wiki/Tres_veces_Ana', '/wiki/La_doble_vida_de_Estela_Carrillo', '/wiki/Me_declaro_culpable', '/w/index.php?title=Ramiro_Fumazoni&action=edit&section=4', '#cite_ref-1', 'https://web.archive.org/web/20171108084039/http://www.univision.com/novelas/tres-veces-ana/ramiro-fumazoni-y-jessica-mass-bautizaron-a-sus-mellizos-fotos', 'http://www.univision.com/novelas/tres-veces-ana/ramiro-fumazoni-y-jessica-mass-bautizaron-a-sus-mellizos-fotos', '#cite_ref-univision_2-0', '#cite_ref-univision_2-1', 'https://web.archive.org/web/20171108084149/http://www.univision.com/novelas/tres-veces-ana/10-cosas-que-debes-saber-de-ramiro-fumazoni-fotos', 'http://www.univision.com/novelas/tres-veces-ana/10-cosas-que-debes-saber-de-ramiro-fumazoni-fotos', '/w/index.php?title=Ramiro_Fumazoni&action=edit&section=5', 'https://www.imdb.com/name/nm4260893/', '/wiki/IMDb', 'https://en.wikipedia.org/w/index.php?title=Ramiro_Fumazoni&oldid=1002937832', '/wiki/Help:Category', '/wiki/Category:1971_births', '/wiki/Category:Living_people', '/wiki/Category:Argentine_male_television_actors', '/wiki/Category:21st-century_Argentine_male_actors', '/wiki/Category:CS1_Spanish-language_sources_(es)', '/wiki/Category:Articles_with_short_description', '/wiki/Category:Short_description_matches_Wikidata', '/wiki/Category:Articles_with_hCards', '/wiki/Category:AC_with_0_elements']]
with dbdb as db:
    db.create_wiki_tables()
    #db.insert_data(test_data)
    db.find_entry_by_title('Ramiro Fumazoni - Wikipedia')"""