import os

foods = [
"Anitta", "Neymar", "Ivete Sangalo", "Pelé", "Xuxa", 
"Gisele Bündchen", "Rodrigo Santoro", "Wesley Safadão", "Paulo Coelho", "Caetano Veloso",
"Adriana Lima", "Fernanda Montenegro", "Luan Santana", "Roberto Carlos", "Marina Ruy Barbosa", 
 "Bruna Marquezine", "Thiaguinho", "Sandy", "Fátima Bernardes", "Daniela Mercury",
"Taís Araújo", "Reynaldo Gianecchini", "Marcos Palmeira", "Juliana Paes", "Luciano Huck",
"Angélica", "Rita Lee", "Gal Costa", "Chico Buarque", "Alcione", 
"Carlinhos Brown", "Ivana Trump", "Rafa Kalimann", "Gusttavo Lima", "Zezé Di Camargo",
"Eduardo Costa", "Fábio Porchat", "Tatá Werneck", "Camila Pitanga", "Regina Casé",
"Lázaro Ramos", "Marília Mendonça", "Simaria", "Simone", "Michel Teló",
"Zeca Pagodinho", "Djavan", "Roberta Miranda", "Alok", "Nando Reis",
"Caetano Veloso", "Maria Bethânia", "Gilberto Gil", "Seu Jorge", "Vanessa da Mata",  
"Beyoncé", "Brad Pitt", "Angelina Jolie", "Leonardo DiCaprio", "Taylor Swift", 
"Elon Musk", "Kim Kardashian", "Cristiano Ronaldo", "Lionel Messi", "Adele",
 "Johnny Depp", "Lady Gaga", "Emma Watson", "Tom Cruise", "Jennifer Lawrence", 
"Rihanna", "Dwayne Johnson", "Justin Bieber", "Meryl Streep", "Drake", 
"Bill Gates", "Oprah Winfrey", "Keanu Reeves", "Selena Gomez", "Chris Hemsworth", 
 "Scarlett Johansson", "Ed Sheeran", "Katy Perry", "LeBron James", "Ariana Grande",
"Shakira", "Jennifer Lopez", "Will Smith", "Margot Robbie", "Chris Evans",
"Robert Downey Jr.", "Samuel L. Jackson", "Tom Hanks", "Gal Gadot", "Cardi B",
"Kanye West", "Megan Thee Stallion", "Zendaya", "Vin Diesel", "Priyanka Chopra",
"Blake Lively", "Ryan Reynolds", "Eminem", "Post Malone", "Billie Eilish",
"Bruno Mars", "Justin Timberlake", "Lizzo", "The Weeknd", "Shawn Mendes",
"Dua Lipa", "Miley Cyrus", "Nicki Minaj", "Harry Styles", "Sam Smith",
"John Legend", "Alicia Keys", "Charlie Puth", "BTS", "BLACKPINK", " "
]

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def user_letter():
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("Only single letters are allowed!")
        else:
            return guess
