import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox


def enter_data():
    accepted = accept_var.get()

    if accepted=="Accepted":

        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            gender = gender_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            #address
            address = address_entry.get()
            contect = contect_entry.get()
            if contect:

                #Email or Passwords
                email = email_entry.get()
                if email:

                    password = password_entry.get()
                    cpassword = confirm_password_entry.get()
                    if password and cpassword:

                        if password != cpassword:
                            tkinter.messagebox.showwarning(title="Error", message="Passwords do not match.")
                            return


                        #ragistation Status and Terms
                        registration_status = reg_status_var.get()


                        print(
                            "First Name: ", firstname,
                            "Last Name: ", lastname,
                            "Gender: ", gender)
                        print(
                            "Age: ", age,
                            "Nationality: ", nationality)
                        print(
                            # address
                            "Address: ", address,
                            "Contect Number: ", contect)
                        print(
                            #email & passwords
                            "Email: ", email,
                            "Password: ", password,
                            "Confirm Password: ", cpassword)
                        print(
                            "Registration Status: ", registration_status 
                        )
                        print("--------------------------------------------------------------------------------------------")
                    else:
                        tkinter.messagebox.showwarning(title="Error", message="Password are required.")
                else:
                    tkinter.messagebox.showwarning(title="Error", message="Email are required.")
            else:
                tkinter.messagebox.showwarning(title="Error", message="Contect Number are required.")    
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and Last name are required.")
    else:
        #print("Error")
        tkinter.messagebox.showwarning(title="Error", message="Your are have not accepted the terms")
    

window = tkinter.Tk()
window.title("Sultan Dine Registation From")

frame = tkinter.Frame(window)
frame.pack()

# Saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

gender_label = tkinter.Label(user_info_frame, text="Gender")
gender_combobox = ttk.Combobox(user_info_frame, values=["Male","Female","Other"])
gender_label.grid(row=0, column=2)
gender_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=10, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Bangladesh","India","Pakistan","London","Africa","Antarctica","Asia","Europe","North America","Oceania","South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# User Address
address_contect_frame = tkinter.LabelFrame(frame)
address_contect_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

address_label = tkinter.Label(address_contect_frame, text="Address")
address_label.grid(row=0, column=0)
address_entry = tkinter.Entry(address_contect_frame, width=50)
address_entry.grid(row=1, column=0,)

contect_label = tkinter.Label(address_contect_frame, text="Contect Number")
contect_label.grid(row=0, column=2)
contect_entry = tkinter.Entry(address_contect_frame)
contect_entry.grid(row=1, column=2,)

for widget in address_contect_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# User Email & Password
email_pass_frame = tkinter.LabelFrame(frame)
email_pass_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

email_label = tkinter.Label(email_pass_frame, text="Email")
email_label.grid(row=0, column=0)
email_entry = tkinter.Entry(email_pass_frame, width=35)
email_entry.grid(row=2, column=0,sticky="ew")

password_label = tkinter.Label(email_pass_frame, text="Password")
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(email_pass_frame)
password_entry.grid(row=4, column=0,sticky="ew")

confirm_password_label = tkinter.Label(email_pass_frame, text="Password Confirm")
confirm_password_label.grid(row=3, column=1)
confirm_password_entry = tkinter.Entry(email_pass_frame, width=25, show='*')
confirm_password_entry.grid(row=4, column=1,sticky="w")



def hide_eye():
    if eye_button['text'] == 'Show':
        confirm_password_entry.config(show='')
        eye_button.config(text='Hide')

    else:
        confirm_password_entry.config(show='*')
        eye_button.config(text='Show')

eye_button = tkinter.Button(email_pass_frame, text="show", command= hide_eye)
eye_button.grid(row=4, column=2,)


for widget in email_pass_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# registation Status
one_time_frame = tkinter.LabelFrame(frame, text="Registration Status")
one_time_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

reg_status_var = tkinter.StringVar(value="Not Registered")

registered_check = tkinter.Checkbutton(one_time_frame, text="Currently Registered",
                                        variable=reg_status_var, onvalue="Registered" , offvalue="Not Registered")

registered_check.grid(row=0, column=0)

for widget in one_time_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# terms and conditon
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions",
                                                    variable=accept_var, onvalue="Accepted", offvalue= "Not Accepted")
terms_check.grid(row=0, column=0)

for widget in terms_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#Button
button = tkinter.Button(frame, text="Register", command = enter_data)
button.grid(row=5, column=0, sticky="news", padx=20, pady=10)


window.mainloop()