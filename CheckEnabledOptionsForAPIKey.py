import tkinter as tk
from tkinter import messagebox, ttk
import base64
import requests
import json

def get_api_key_details(api_key):
    loginString = api_key + ":"
    encodedBytes = base64.b64encode(loginString.encode())
    encodedUserPassSequence = str(encodedBytes, 'utf-8')
    authorizationHeader = "Basic " + encodedUserPassSequence

    apiEndpoint_Url = "https://cloud.gravityzone.bitdefender.com/api/v1.0/jsonrpc/general"

    request = {
        "params": {},
        "jsonrpc": "2.0",
        "method": "getApiKeyDetails",
        "id": "787b5e36-89a8-4353-88b9-6b7a32e9c87f"
    }

    try:
        result = requests.post(apiEndpoint_Url, json=request, verify=True, headers={"Content-Type": "application/json", "Authorization": authorizationHeader})
        response = result.text
        display_response(response)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def display_response(response):
    response_json = json.loads(response)
    formatted_response = json.dumps(response_json, indent=4)
    response_text.config(state='normal')  # Set state to 'normal' to allow insertion
    response_text.delete(1.0, tk.END)
    response_text.insert(tk.END, formatted_response)
    response_text.config(state='disabled')

# Create main window
root = tk.Tk()
root.title("API Key Details")

# Dark mode
root.tk_setPalette(background="black", foreground="white")

# Create response frame
response_frame = tk.Frame(root, bg='black')
response_frame.pack(pady=10)

# API Key entry
api_key_label = tk.Label(response_frame, text="API Key:", bg='black', fg='white')
api_key_label.pack()

api_key_entry = tk.Entry(response_frame, width=50, bg='white', fg='black')
api_key_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(response_frame, text="Check the API key", command=lambda: get_api_key_details(api_key_entry.get()))
submit_button.pack(pady=5)

# Response text widget
response_text = tk.Text(response_frame, width=80, height=20, bg='gray49', fg='black', state='disabled')
response_text.pack(padx=5, pady=5)

root.mainloop()