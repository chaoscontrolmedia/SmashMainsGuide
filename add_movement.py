import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('smash.db')
cursor = conn.cursor()

# Define the INSERT statement with parameters for Moveset
insert_moveset_query = "INSERT INTO movesets (ground_attacks, aerial_attacks, special_attacks, grab_throws) VALUES (?, ?, ?, ?)"

# Define the parameters for the INSERT statement for Moveset
moveset_data = ("Ground Attacks", "Aerial Attacks", "Special Attacks", "Grab Throws")

# Execute the INSERT statement for Moveset
cursor.execute(insert_moveset_query, moveset_data)

# Define the INSERT statement with parameters for SpecialAttacks
insert_special_attacks_query = "INSERT INTO special_attacks (neutral_special, side_special, up_special, down_special) VALUES (?, ?, ?, ?)"

# Define the parameters for the INSERT statement for SpecialAttacks
special_attacks_data = ("Neutral Special", "Side Special", "Up Special", "Down Special")

# Execute the INSERT statement for SpecialAttacks
cursor.execute(insert_special_attacks_query, special_attacks_data)

# Define the INSERT statement with parameters for GroundAttacks
insert_ground_attacks_query = "INSERT INTO ground_attacks (jab, forward_tilt, up_tilt, down_tilt, forward_smash, up_smash, down_smash) VALUES (?, ?, ?, ?, ?, ?, ?)"

# Define the parameters for the INSERT statement for GroundAttacks
ground_attacks_data = ("Jab", "Forward Tilt", "Up Tilt", "Down Tilt", "Forward Smash", "Up-Smash", "Down Smash")

# Execute the INSERT statement for GroundAttacks
cursor.execute(insert_ground_attacks_query, ground_attacks_data)

# Define the INSERT statement with parameters for AerialAttacks
insert_aerial_attacks_query = "INSERT INTO aerial_attacks (neutral_air, forward_air, back_air, up_air, down_air) VALUES (?, ?, ?, ?, ?)"

# Define the parameters for the INSERT statement for AerialAttacks
aerial_attacks_data = ("Neutral Air", "Forward Air", "Back Air", "Up Air", "Down-Air")

# Execute the INSERT statement for AerialAttacks
cursor.execute(insert_aerial_attacks_query, aerial_attacks_data)

# Define the INSERT statement with parameters for GrabThrows
insert_grab_throws_query = "INSERT INTO grab_throws (grab, dash_grab, pivot_grab, pummel, forward_throw, backward_throw, up_throw, down_throw) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

# Define the parameters for the INSERT statement for GrabThrows
grab_throws_data = ("Grab", "Dash Grab", "Pivot Grab", "Pummel", "Forward Throw", "Backward Throw", "Up-Throw", "Down-Throw")

# Execute the INSERT statement for GrabThrows
cursor.execute(insert_grab_throws_query, grab_throws_data)

# Commit the transaction (save changes to the database)
conn.commit()

# Close the database connection
conn.close()

print("Moveset and attacks added successfully!")
