import sqlite3


class Sqlrequests():

    def __init__(self):
        self.db = None
        self.sql = None
        self.create_db()

    def create_db(self):
        self.db = sqlite3.connect('./SWGdb.sqlite')
        self.sql = self.db.cursor()
        self.sql.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER ,name TEXT, credit INTEGER)")
        self.sql.execute("CREATE TABLE IF NOT EXISTS units (owner_id INTEGER, type TEXT, amount INTEGER, skill INTEGER,\
        era INTEGER)")

        self.db.commit()

    def new_player(self, user):
        if self.sql.execute("SELECT name FROM users WHERE id = ? ", (user.id,)).fetchone() is None:
            self.sql.execute("INSERT INTO users VALUES (?,?,?)", (user.id, user.name, 1000))
            self.sql.execute("INSERT INTO units VALUES (?,?,?,?,?)", (user.id, 'sapper', 160, '0', '0'))
            self.sql.execute("INSERT INTO units VALUES (?,?,?,?,?)", (user.id, 'cavalryman', 40, '0', '0'))
            self.db.commit()

            return True
        else:
            return False

    def unit_list(self, user: str = None, nation: str = None, unit_id: int = None):
        if user is not None:
            return self.sql.execute("SELECT subtype, amount, skill, era FROM units WHERE owner_id = ?", (user.id,)). \
                fetchall()

        elif nation is not None:
            return self.sql.execute("SELECT id,type,hp,infantry_damage,armveh_damage,aircrafts_damage,count_carry,\
            supplie,artillery,carry FROM stats WHERE nation = ?", (nation,)).fetchall()

        elif self.sql.execute('SELECT id FROM stats WHERE  id = ?', (unit_id,)).fetchall():
            return True

    def hiring(self, unit_id: int = None, user_id: int = None):
        users_credits = self.sql.execute("SELECT credit FROM users WHERE id = ?", (user_id,)).fetchone()[0]
        units_cost = self.sql.execute("SELECT credit FROM users WHERE id = ?", (user_id,)).fetchone()[0]
        if self.sql.execute("SELECT credit FROM users WHERE id = ?", (user_id,)).fetchone()[0]:
            pass


sqlreq = Sqlrequests()
