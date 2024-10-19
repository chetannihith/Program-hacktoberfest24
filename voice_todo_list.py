import speech_recognition as sr
import tkinter as tk

recognizer = sr.Recognizer()

def listen_and_add():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        recognizer.energy_threshold = 10000
        recognizer.adjust_for_ambient_noise(source, 1.2)
        
        try:
            command = recognizer.recognize_google(audio)
            listbox.insert(tk.END, command)  # Add recognized voice command to the listbox
            speak("Task added: " + command)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, there was an error with the service.")


def speak(text):
    print(text)

# Tkinter function to add task via typing
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    try:
        selected_task = listbox.curselection()
        listbox.delete(selected_task)
    except:
        speak("Please select a task to remove.")


# Create the main window
root = tk.Tk()
root.title("Voice-Controlled To-Do List")

# Entry widget to input tasks manually
entry = tk.Entry(root, width=35)
entry.pack(pady=10)

# Button to add task via typing
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Button to add task via voice
voice_button = tk.Button(root, text="Add Task by Voice", command=listen_and_add)
voice_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)


listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)


root.mainloop()