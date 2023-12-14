from socket import socket, AF_INET, SOCK_STREAM

# List of quiz questions with options
quiz_questions = (
    "Which planet is closest to the Sun in our Solar System?\nA) Mars\nB) Venus\nC) Jupiter\nD) Uranus\n",
    "The highest mountain on Earth, located in the Himalayas, is how many meters tall?\nA) 7,201 meters\nB) 8,848 meters\nC) 6,962 meters\nD) 9,356 meters\n",
    "Which author is known for classic works such as 'Les Misérables' and 'The Hunchback of Notre-Dame'?\nA) Charles Dickens\nB) Jane Austen\nC) Victor Hugo\nD) Fyodor Dostoyevsky\n"
)

# Function to handle the client's quiz attempt
def manage_quiz(client_socket):
    # Server-side answer input (retaining original behavior for illustration)
    correct_answers = input("Enter the correct answers: ").strip()
    # Client response reception
    client_answer = client_socket.recv(1024).decode().strip()

    # Send response based on answers
    if correct_answers.lower() == 'bbc':
        client_socket.sendall("Congratulations!! You're a millionaire now".encode())
    elif not correct_answers:
        client_socket.sendall("Data didn't come!!!".encode())
    else:
        client_socket.sendall("Sorry!!! You lost the competition".encode())

# Function to run the quiz server indefinitely
def run_quiz_server():
    # Set up the server socket
    with socket(AF_INET, SOCK_STREAM) as quiz_server:
        quiz_server.bind(('127.0.0.1', 8888))
        quiz_server.listen(5)
        print("Quiz Server running on port 8888...")

        while True:
            # Accept new clients
            client_sock, addr = quiz_server.accept()
            print(f"New connection from {addr}")
            with client_sock:
                # Send quiz questions to the client
                for question in quiz_questions:
                    client_sock.sendall(question.encode())
                # Process the client's quiz responses
                manage_quiz(client_sock)

# Check if the script is the main program
if __name__ == '__main__':
    run_quiz_server()