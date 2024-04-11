import sqlite3


# Connect to the SQLite database
conn = sqlite3.connect('smash.db')
cursor = conn.cursor()

# Define the ALTER TABLE statement to add the overview column
alter_table_query = "ALTER TABLE fighters ADD COLUMN overview TEXT"

# Execute the ALTER TABLE statement to add the overview column
cursor.execute(alter_table_query)

# Define the INSERT statement with parameters
insert_query = "INSERT INTO fighters (name, strengths, weaknesses, overview) VALUES (?, ?, ?, ?)"

# Define the list of fighter data to be inserted
fighters_data = [
    ("Mario", "Versatile Moveset", "Limited Range", "Mario is a versatile character with decent speed and great combo potential. You need to get in close and harass the enemy. Mario also has tools to stuff the enemy's recovery, like his FLUDD, Cape, Fireball, and his Forward Air spike."),
    ("Chrom", "Powerful Sword Attacks", "Poor recovery", "Chrom is the main protagonist of Fire Emblem Awakening. He is a powerful swordsman with high damage output."),
    ("Fox", "Fast and Agile", "Lightweight", "Fox is a fast and agile fighter with quick attacks and good mobility. He excels at rushing down opponents and applying pressure with his Blaster and Illusion techniques."),
    ("Wolf", "Strong Attacks", "Slow mobility", "Wolf is a heavyweight fighter with strong attacks and good aerial mobility. He can apply pressure with his Blaster and mix up his approach with his Wolf Flash."),
    ("Sephiroth", "Long-range Attacks", "Lightweight", "Sephiroth is a long-range fighter with powerful attacks and good aerial mobility. He can control space with his Masamune and apply pressure with his Flare and Shadow Flare."),
    ("Little Mac", "Hard-Hitting", "Weak aerial game", "Little Mac is a hard-hitting boxer with strong ground attacks and a weak aerial game. He excels at close-range combat and can punish opponents with his KO Punch.")
]

# Execute the INSERT statement for each fighter
for fighter_data in fighters_data:
    cursor.execute(insert_query, fighter_data)

# Commit the transaction (save changes to the database)
conn.commit()

# Retrieve and print the details of all the newly added fighters
cursor.execute("SELECT * FROM fighters")
new_fighters = cursor.fetchall()

print("New Fighters Details:")
for fighter in new_fighters:
    print("Name:", fighter[1])
    print("Strengths:", fighter[2])
    print("Weaknesses:", fighter[3])
    print("Overview:", fighter[4])
    print()  # Add an empty line for better readability

# Close the database connection
conn.close()

print("Fighters added successfully!")