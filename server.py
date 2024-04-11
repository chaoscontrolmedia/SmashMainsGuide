import sqlite3
from flask import Flask, render_template, send_from_directory
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smash.db'
#db = SQLAlchemy(app)


class Fighter():
    def __init__(self,id, name, strengths, weaknesses, overview):
        self.id = id
        self.name = name
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.overview = overview

    def fighter_name(self):
        return self.name
    

    def fighter_strengths(self):
        return self.strengths
    
    def fighter_weaknesses(self):
        return self.weaknesses
    
    '''
    def fighter_weaknesses(self):
        return "Weaknesses: {}".format(self.strengths)
        '''
    
#The ground attack attributes
class GroundAttacks:
    def __init__(self):
        self.jab = "Jab"
        self.forward_tilt = "Forward Tilt"
        self.up_tilt = "Up Tilt"
        self.down_tilt = "Down Tilt"
        self.forward_smash = "Forward Smash"
        self.up_smash = "Up-Smash"
        self.down_smash = "Down Smash"

class AerialAttacks:
    def __init__(self):
        self.neutral_air = "Neutral Air"
        self.forward_air = "Forward Air"
        self.back_air = "Back Air"
        self.up_air = "Up Air"
        self.down_air = "Down-Air"

class SpecialAttacks:
    def __init__(self, neutral_special=None, side_special=None, up_special=None, down_special=None):
        self.neutral_special = neutral_special or "Neutral Special"
        self.side_special = side_special or "Side Special"
        self.up_special = up_special or "Up Special"
        self.down_special = down_special or "Down Special"

class GrabThrows:
    def __init__(self):
        self.grab = "Grab"
        self.dash_grab = "Dash Grab"
        self.pivot_grab = "Pivot Grab"
        self.pummel = "Pummel"
        self.forward_throw = "Forward Throw"
        self.backward_throw = "Backward Throw"
        self.up_throw = "Up-Throw"
        self.down_throw = "Down-Throw"


#  a class with default constructors 
class Moveset:
    def __init__(self, ground_attacks=None, aerial_attacks=None, special_attacks=None, grab_throws=None):
        self.ground_attacks = ground_attacks or GroundAttacks()
        self.aerial_attacks = aerial_attacks or AerialAttacks()
        self.special_attacks = special_attacks or SpecialAttacks()
        self.grab_throws = grab_throws or GrabThrows()


# Custom special attacks for Chrom
chrom_special_attacks = SpecialAttacks(
    neutral_special="Flare Blade",
    side_special="Double-Edge Dance",
    up_special="Soaring Slash",
    down_special="Counter"
)

wolf_special_attacks = SpecialAttacks(
    neutral_special="Blaster",
    side_special="Wolf Flash",
    up_special="Fire Wolf",
    down_special="Reflector"
)

sephiroth_special_attacks = SpecialAttacks(
    neutral_special="Flare",
    side_special="Shadow Flare",
    up_special="Blade Dash",
    down_special="Scintilla"
)

mario_special_attacks = SpecialAttacks(
    neutral_special="Fireball",
    side_special="Cape",
    up_special="Super Jump Punch",
    down_special="F.L.U.D.D."
)

fox_special_attacks = SpecialAttacks(
    neutral_special="Blaster",
    side_special="Fox Illusion",
    up_special="Fire Fox",
    down_special="Reflector"
)

















    


# Create the fighters table if it doesn't exist
def create_fighters_table():
    try:
        conn = sqlite3.connect('smash.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS fighters (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            strengths TEXT,
                            weaknesses TEXT
                        )''')
        conn.commit()
    except Exception as e:
        print(f"Error occurred while creating fighters table: {e}")
    finally:
        conn.close()

# Call the function to create the fighters table when the application starts
create_fighters_table()





# Instantiate Attacks once
aerial_attacks = AerialAttacks()
ground_attacks = GroundAttacks()
special_attacks = SpecialAttacks()
grab_throws = GrabThrows()

# Create Moveset instances for each fighter with custom special attacks
ChromMoveset = Moveset(ground_attacks, aerial_attacks, chrom_special_attacks, grab_throws)
FoxMoveset = Moveset(ground_attacks, aerial_attacks, fox_special_attacks, grab_throws)
MarioMoveset = Moveset(ground_attacks, aerial_attacks, mario_special_attacks, grab_throws)
WolfMoveset = Moveset(ground_attacks, aerial_attacks, wolf_special_attacks, grab_throws)
SephirothMoveset = Moveset(ground_attacks, aerial_attacks, sephiroth_special_attacks, grab_throws)
LittleMacMoveset = Moveset(ground_attacks, aerial_attacks, sephiroth_special_attacks, grab_throws)


mario_overview = "Mario is a versatile character with decent speed and great combo potential. You need to get in close and harass the enemy. Mario also has tools to stuff the enemy's recovery, like his FLUDD, Cape, Fireball, and his Forward Air spike."

chrom_overview = "Chrom is a fast and powerful swordfighter with a straightforward playstyle. He excels at close-quarters combat and has strong offensive capabilities."

fox_overview = "Fox is a fast and agile character known for his quick movements and strong combo potential. He excels at close-range combat and relies on his speed to outmaneuver opponents."

wolf_overview = "Wolf is a versatile character with a balanced mix of speed, power, and range. He excels at controlling space with his blaster and has strong aerial attacks."
little_mac_overview = "Little Mac is a ground-based fighter with incredible speed and power on the ground but limited options in the air. He excels at close-quarters combat and has strong KO potential."
sephiroth_overview = "Sephiroth is a unique fighter with a long-reaching sword and powerful special moves. He excels at spacing and zoning opponents with his long-range attacks."

'''
Test views
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/about/<username>')
def about_page(username):
    return f'This is about {username}'
'''




# Instances of the Fighter class with general details
Chrom = Fighter(1, 'Chrom', 'Powerful Sword Attacks', 'Poor recovery',chrom_overview)
LittleMac = Fighter(2, 'Little Mac', 'Hard-Hitting', 'Weak aerial game',little_mac_overview)
Fox = Fighter(3, 'Fox', 'Fast and Agile', 'Lightweight',fox_overview)
Mario = Fighter(4, 'Mario', 'Versatile Moveset', 'Limited Range',mario_overview)
Wolf = Fighter(5, 'Wolf', 'Strong Attacks', 'Slow mobility',wolf_overview)
Sephiroth = Fighter(6, 'Sephiroth', 'Long-range Attacks', 'Lightweight',sephiroth_overview)

# Raw SQL Query example
def get_fighter_by_name(name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('smash.db')
        cursor = conn.cursor()

        # Execute a parameterized query
        query = "SELECT * FROM fighter WHERE name = ?"
        cursor.execute(query, (name,))
        
        # Fetch the first result
        fighter = cursor.fetchone()

        # Close the database connection
        conn.close()

        return fighter
    except Exception as e:
        # Handle exceptions, log the error, or return a default value
        print(f"Error occurred while fetching fighter: {e}")
        return None




# Define a route to serve images
@app.route('/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')



@app.route("/mario")
def mario_page():
    try:
        # Connect to the SQLite database
        with sqlite3.connect('smash.db') as conn:
            cursor = conn.cursor()

            # Execute a raw SQL query to fetch data
            cursor.execute("SELECT * FROM fighters WHERE name = 'Mario'")
            fighter_data = cursor.fetchone()

            if fighter_data:
                # Instantiate a Fighter object using the fetched data
                fighter = Fighter(*fighter_data)
            else:
                fighter = None

        # Pass the fetched data to the template
        return render_template('mario.html', 
                               fighter=fighter, 
                               overview=mario_overview,
                               ground_moves=vars(MarioMoveset.ground_attacks).values(),
                               aerial_moves=vars(MarioMoveset.aerial_attacks).values(),
                               special_moves=vars(MarioMoveset.special_attacks).values(),
                               grab_throws=vars(MarioMoveset.grab_throws).values())

    except Exception as e:
        # Handle exceptions, log the error, or return an error page
        print(f"Error occurred while fetching Mario: {e}")
        return render_template('error.html', error_message='An error occurred while fetching Mario.')



@app.route("/fox")
def fox_page():
    try:
        with sqlite3.connect('smash.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fighters WHERE name = 'Fox'")
            fighter_data = cursor.fetchone()

            if fighter_data:
                fighter = Fighter(*fighter_data)
            else:
                fighter = None

        return render_template('fox.html', 
                               fighter=fighter, 
                               overview=fox_overview,
                               ground_moves=vars(FoxMoveset.ground_attacks).values(),
                               aerial_moves=vars(FoxMoveset.aerial_attacks).values(),
                               special_moves=vars(FoxMoveset.special_attacks).values(),
                               grab_throws=vars(FoxMoveset.grab_throws).values())

    except Exception as e:
        print(f"Error occurred while fetching Fox: {e}")
        return render_template('error.html', error_message='An error occurred while fetching Fox.')

    



@app.route("/chrom")
def chrom_page():
    try:
        with sqlite3.connect('smash.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fighters WHERE name = 'Chrom'")
            fighter_data = cursor.fetchone()

            if fighter_data:
                fighter = Fighter(*fighter_data)
            else:
                fighter = None

        return render_template('chrom.html', 
                               fighter=fighter, 
                               overview=chrom_overview,
                               ground_moves=vars(ChromMoveset.ground_attacks).values(),
                               aerial_moves=vars(ChromMoveset.aerial_attacks).values(),
                               special_moves=vars(ChromMoveset.special_attacks).values(),
                               grab_throws=vars(ChromMoveset.grab_throws).values())

    except Exception as e:
        print(f"Error occurred while fetching Chrom: {e}")
        return render_template('error.html', error_message='An error occurred while fetching Chrom.')



@app.route("/wolf")
def wolf_page():
    try:
        with sqlite3.connect('smash.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fighters WHERE name = 'Wolf'")
            fighter_data = cursor.fetchone()

            if fighter_data:
                fighter = Fighter(*fighter_data)
            else:
                fighter = None

        return render_template('wolf.html', 
                               fighter=fighter, 
                               overview=wolf_overview,
                               ground_moves=vars(WolfMoveset.ground_attacks).values(),
                               aerial_moves=vars(WolfMoveset.aerial_attacks).values(),
                               special_moves=vars(WolfMoveset.special_attacks).values(),
                               grab_throws=vars(WolfMoveset.grab_throws).values())

    except Exception as e:
        print(f"Error occurred while fetching Wolf: {e}")
        return render_template('error.html', error_message='An error occurred while fetching Wolf.')


@app.route("/sephiroth")
def sephiroth_page():
    try:
        with sqlite3.connect('smash.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fighters WHERE name = 'Sephiroth'")
            fighter_data = cursor.fetchone()

            if fighter_data:
                fighter = Fighter(*fighter_data)
            else:
                fighter = None

        return render_template('sephiroth.html', 
                               fighter=fighter, 
                               overview=sephiroth_overview,
                               ground_moves=vars(SephirothMoveset.ground_attacks).values(),
                               aerial_moves=vars(SephirothMoveset.aerial_attacks).values(),
                               special_moves=vars(SephirothMoveset.special_attacks).values(),
                               grab_throws=vars(SephirothMoveset.grab_throws).values())

    except Exception as e:
        print(f"Error occurred while fetching Sephiroth: {e}")
        return render_template('error.html', error_message='An error occurred while fetching Sephiroth.')

@app.route("/little_mac")
def little_mac_page():
    try:
        with sqlite3.connect('smash.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fighters WHERE name = 'Little Mac'")
            fighter_data = cursor.fetchone()

            if fighter_data:
                fighter = Fighter(*fighter_data)
            else:
                fighter = None
        return render_template('little_mac.html', 
                        fighter=fighter, 
                        overview=little_mac_overview,
                        ground_moves=vars(LittleMacMoveset.ground_attacks).values(),
                        aerial_moves=vars(LittleMacMoveset.aerial_attacks).values(),
                        special_moves=vars(LittleMacMoveset.special_attacks).values(),
                        grab_throws=vars(LittleMacMoveset.grab_throws).values())



    except Exception as e:
        print(f"Error occurred while fetching Little Mac: {e}")
        return render_template('error.html', error_message='An error occurred while fetching Little Mac.')

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    #debug=true-Dev Server
    app.run(debug=True)
    


