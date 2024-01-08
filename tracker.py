from tkinter import Tk, Button, Label, Entry
import requests
import webbrowser
import datetime as dt

USERNAME = "nhatek"
TOKEN = "PQ88wP1grYE2"
GRAPH_ID = "reading1"


URL = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}'

graph_headers = {
    'X-USER-TOKEN': TOKEN
}


def submit():
    value_params = {
        'date': dt.datetime.now().strftime("%Y%m%d"),
        'quantity': report_entry.get(),
    }

    requests.post(url=URL, headers=graph_headers, json=value_params)
    webbrowser.open(f'{URL}.html')


window = Tk()
window.title("Habit Tracker")
window.config(padx=25, pady=25)

title_label = Label(text="Reading Tracker", font=['Arial', 18, 'bold'])
report_label = Label(width=15, text="Total Pages Read:", font=['Arial', 12, 'normal'])
submit_button = Button(width=20, text="Submit", command=submit)
report_entry = Entry(width=35)

title_label.grid(row=0, column=0, columnspan=2)
report_label.grid(row=2, column=0, sticky='EW')
report_entry.grid(row=2, column=1, sticky='EW')
submit_button.grid(row=3, column=0, columnspan=2)
window.mainloop()
