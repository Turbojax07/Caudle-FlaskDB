import psycopg2
import os

print('Setting up database connection...')

# Login Creds
# These depend on the internet I am connected to.
# If at school, use these creds:
# DB: "campbejs1db", DB_UN: "campbejs1", DB_PW: "41631", DB_HN: "s2c-cit-b112", DB_PORT: "5432"
# If not at school and on personal laptop, use these creds:
# DB: "turbo", DB_UN: "turbo", DB_PW: "toor", DB_HN: "localhost", DB_PORT: "5000"
database = os.environ["DB"     ]
username = os.environ["DB_UN"  ]
password = os.environ["DB_PW"  ]
hostname = os.environ["DB_HN"  ]
port     = os.environ["DB_PORT"]

# Setting up the connection
conn = psycopg2.connect(database=database, user=username, password=password, host=hostname, port=port)

# Getting the cursor
cursor = conn.cursor()

# Loop to continuously read input
while (True):
    # Getting input from the user
    prompt = input(f"{username}@{hostname}=> ")

    # Exiting the program if the user enters "exit" bc slash commands don't work
    if prompt == "exit":
        break

    # Clearing the console if the user enters "clear" or "cls" (also bc slash commands don't work)
    elif prompt == "cls" or prompt == "clear":
        os.system("cls")
        print("\033[0m")

    else:
        # The program errors out if the command is incorrect.
        # This handles that and just prints the error rather than executing it.
        try:
            # Executing the input
            cursor.execute(prompt.encode())

            # Saving the changes (if any)
            conn.commit()

            # The program errors out if the command had no results. (EX: "CREATE DATABASE dept")
            # This handles that and simulates the output that postgres would show.
            try:
                # Printing results
                print(cursor.fetchall())
            except (psycopg2.ProgrammingError):
                print(prompt.split(" ")[0] + " " + prompt.split(" ")[1])
        except (psycopg2.errors.SyntaxError) as err:
            print(err)
    
# One final save
conn.commit()

# Exiting the program
cursor.close()
conn.close()