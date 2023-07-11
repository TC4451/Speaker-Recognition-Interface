import tkinter as tk
from sound_recording import record_sample

root = tk.Tk()
root.geometry('600x400')
root.title('Speaker Recognition')

# record the sample audio and save it to the sample directory
def save_sample(entry):
    name = entry.get()
    record_sample(5, "./speaker_voice_sample/"+name+".wav")

# call enrollment page
def enrollment_page():
    enrollment_frame = tk.Frame(main_frame)

    # # for testing
    # lb = tk.Label(enrollment_frame, text = 'enrollment frame', font=('Bold', 30))
    # lb.pack()

    enroll_entry = tk.Entry(main_frame)
    enroll_entry.pack(expand=True, anchor="center")

    enroll_btn = tk.Button(enrollment_frame, text='Enroll', font=('Bold', 15),
                            fg='#158aff', bd=0,
                            command=lambda:save_sample(enroll_entry))
    # enroll_btn.place(relx=0.5, rely=0.5, anchor="center")
    enroll_btn.pack(expand=True, anchor="center")
    
    enrollment_frame.pack(pady=20)

# call recognition page
def recognition_page():
    recognition_frame = tk.Frame(main_frame)

    lb = tk.Label(recognition_frame, text = 'recognition frame', font=('Bold', 30))
    lb.pack()
    recognition_frame.pack(pady=20)

def hide_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

# hide all indicatros
def hide_indicator():
    enroll_indicate.config(bg='#c3c3c3')
    recognition_indicate.config(bg='#c3c3c3')

# show the selected page's indicator
def indicate(label, page):
    hide_indicator()
    label.config(bg='#158aff')
    hide_page()
    page()

# create a frame for the pages options
options_frame = tk.Frame(root, bg='#c3c3c3')

# create pages
enroll_page_btn = tk.Button(options_frame, text='Enrollment', font=('Bold', 15), 
                       fg='#158aff', bd=0, bg='#c3c3c3',
                       command=lambda:indicate(enroll_indicate, enrollment_page))
enroll_page_btn.place(x=10, y=50)

recognition_page_btn = tk.Button(options_frame, text='Recognition', font=('Bold', 15), 
                       fg='#158aff', bd=0, bg='#c3c3c3',
                       command=lambda:indicate(recognition_indicate, recognition_page))
recognition_page_btn.place(x=10, y=100)

# create indicators
enroll_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
enroll_indicate.place(x=3, y=50, width=5, height=35)

recognition_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
recognition_indicate.place(x=3, y=100, width=5, height=35)

# make a frame to contain all options for pages
options_frame.pack(side=tk.LEFT)
# allow frame to be resized
options_frame.pack_propagate(False)
options_frame.configure(width=150, height=400)

# edit the main frame
main_frame = tk.Frame(root, highlightbackground='black',
                      highlightthickness=1)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=500, height=400)

root.mainloop()