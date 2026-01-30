import sqlite3
import gradio as gr

def fetch_phillies():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT playerID
        FROM batting
        WHERE yearID = 1976 and teamID = 'PHI'
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()

    players = []
    for record in records:
        players.append(record[0])
    return players

def f(player):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT HR
        FROM batting
        WHERE playerID = ? and yearID = 1976 and teamID = 'PHI'
    """
    cursor.execute(query,[player])
    records = cursor.fetchall()
    conn.close()
    #return f"Player {player} hit {records[0][0]} home runs in 1976 for the Philadelphia Phillies."
    return records[0][0]

print(f('schmimi01'))

#iface = gr.Interface(fn=f,
#    inputs=gr.Dropdown(choices=fetch_phillies(), label="Player ID"),
#    outputs=gr.Textbox(label="Home Runs"),
#    title="1976 Philadelphia Phillies Home Runs",
#    description="Fetches and displays home runs for a selected 1976 Philadelphia Phillies player.")

#    iface.launch()