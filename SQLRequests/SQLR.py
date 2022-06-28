import sqlite3


class Sqlrequests:

    def __init__(self):
        self.db = None
        self.sql = None
        self.create_db()

    def create_db(self):
        self.db = sqlite3.connect('./SWGdb.sqlite')
        self.sql = self.db.cursor()
        self.sql.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER ,name TEXT, credit INTEGER)")
        self.sql.execute(
            """CREATE TABLE IF NOT EXISTS units (
            owner_id INTEGER, unit_id INTEGER, 
            amount INTEGER, skill INTEGER,
            era INTEGER)""")
        self.sql.execute(
            """CREATE TABLE IF NOT EXISTS stats (
            id INTEGER, nation TEXT,
            type TEXT, hp REAL,
            infantry_damage REAL, armveh_damage REAL,
            aircrafts_damage REAL, count_carry INTEGER,
            supplie REAL, artillery INTEGER,
            carry NUMERIC, cost INTEGER)""")

        self.db.commit()

    def balance(self, user_id: int = None):
        if user_id is not None:
            return self.sql.execute("SELECT credit FROM users WHERE id = ?", (user_id,)).fetchone()[0]

    def awarding(self, user_id: int = None, amount: int = None):
        self.sql.execute("UPDATE users SET credit = credit + ? WHERE id = ?", (amount, user_id))
        self.db.commit()

    def new_player(self, user):
        if self.sql.execute("SELECT name FROM users WHERE id = ? ", (user.id,)).fetchone() is None:
            self.sql.execute("INSERT INTO users VALUES (?,?,?)", (user.id, user.name, 1000))
            self.sql.execute("INSERT INTO units VALUES (?,?,?,?,?)", (user.id, 4, 160, 0, 0))
            self.sql.execute("INSERT INTO units VALUES (?,?,?,?,?)", (user.id, 5, 40, 0, 0))
            self.db.commit()

            return True
        else:
            return False

    def unit_amount(self, user_id: int = None, unit: id = None):
        return self.sql.execute("SELECT amount FROM units WHERE owner_id = ? and unit_id = ?",
                                (user_id, unit)).fetchone()[0]

    def user(self, member_id):
        return True if self.sql.execute("SELECT id FROM users WHERE id = ?", (member_id,)).fetchone() else False

    def unit_list(self, user: object = None, nation: str = None, unit_id: int = None):

        if user is not None:
            return self.sql.execute("SELECT unit_id, amount, skill, era FROM units WHERE owner_id = ?",
                                    (user.id,)).fetchall()

        elif nation is not None:
            return self.sql.execute("SELECT id,type,hp,infantry_damage,armveh_damage,aircrafts_damage,count_carry,\
            supplie,artillery,carry FROM stats WHERE nation = ?", (nation,)).fetchall()

        elif self.sql.execute('SELECT id FROM stats WHERE  id = ?', (unit_id,)).fetchall():
            return True

    def unit_name(self, unit_id: int = None):
        return self.sql.execute("SELECT type FROM stats WHERE id = ?", (unit_id,)).fetchone()[0]

    def hiring(self, unit_id: int = None, user: object = None, count: int = 1):
        if count <= 0:
            raise ValueError
        else:
            users_credits = self.sql.execute("SELECT credit FROM users WHERE id = ?", (user.id,)).fetchone()[0]
            units = self.sql.execute("SELECT cost, type FROM stats WHERE id = ?", (unit_id,)).fetchone()
            if users_credits > units[0] * count:
                self.sql.execute("UPDATE users SET credit = credit - ? WHERE id = ?", (units[0] * count, user.id,))
                if self.sql.execute("SELECT amount FROM units WHERE owner_id = ? AND unit_id = ?",
                                    (user.id, unit_id)).fetchone() is not None:
                    self.sql.execute("UPDATE units SET amount = amount + ? WHERE owner_id = ? AND unit_id = ?",
                                     (12 * count, user.id, unit_id))
                else:
                    self.sql.execute("INSERT INTO units VALUES (?,?,?,?,?)", (user.id, unit_id, 12 * count, 0, 0))
                self.db.commit()
                return units[1]
            else:

                raise NotEnoughMoney(user.name)


sqlreq = Sqlrequests()


class NotEnoughMoney(BaseException):
    def __init__(self, user="User"):
        self.usr = user
        super().__init__(self.usr)

    def __str__(self):
        return f'{self.usr} not enough money for hiring new units'
