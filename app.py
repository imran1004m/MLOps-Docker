from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
greeted_users = []  # Store greeted users in memory

@app.route('/')
def index():
    return '''
        <html>
        <body>
            <h2>Enter your name</h2>
            <form action="/greet" method="POST">
                <input type="text" name="username" placeholder="Your name">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username'].strip()

    if not username:
        return '''
            <html>
            <body>
                <h2 style="color:red;">Name cannot be empty.</h2>
                <a href="/">Go back</a>
            </body>
            </html>
        '''

    greeted_users.append(username)

    # Time-based greeting
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    users_list_html = ''.join(f'<li>{user}</li>' for user in greeted_users)

    return f'''
        <html>
        <body>
            <h2>{greeting}, {username}!</h2>
            <p>Welcome to this app for Docker demonstration.</p>
            <p>Please consider liking and subscribing to the channel.</p>

            <h3>Users greeted so far:</h3>
            <ul>
                {users_list_html}
            </ul>

            <a href="/">Go back</a>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
