import dis
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Function to log the conversion into a Notepad file
def log_conversion(python_code, assembly_code):
    try:
        with open("C:\\Users\\hellh\\OneDrive\\Desktop\\CBPAA\\conversion_log.txt" , "a") as file:
            # change the location of the file to where you want to create the log file.
            file.write("Python Code:\n")
            file.write(python_code)
            file.write("Assembly code:\n")
            file.write(assembly_code)
            file.write("\n\n")
        messagebox.showinfo("Info", "Conversion logged successfully in conversion_log.txt")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while logging the conversion: {e}")

# Function to convert Python code to assembly code
def convert_to_assembly():
    python_code = code_text.get("1.0", tk.END)
    assembly_code = ""

    try:
        # Compile Python code
        code_obj = compile(python_code, '<string>', 'exec')

        # Create a StringIO object to capture disassembly output
        import io
        output_stream = io.StringIO()

        # Redirect stdout to the StringIO object
        import sys
        sys.stdout = output_stream

        # Disassemble Python bytecode
        dis.dis(code_obj)

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Get the disassembly output
        assembly_output = output_stream.getvalue()

        # Concatenate assembly output
        assembly_code = assembly_output

        # Log the conversion into the Notepad file
        log_conversion(python_code, assembly_code)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    # Display the assembly code
    assembly_text.delete("1.0", tk.END)
    assembly_text.insert(tk.END, assembly_code)

# Create GUI
root = tk.Tk()
root.title("Python to Assembly Converter")
root.configure(bg="gray")

# Input frame
input_frame = tk.Frame(root, bg='black')
input_frame.pack(pady=10)

code_label = tk.Label(input_frame, text="Enter Python code:", fg="white", bg="black")
code_label.grid(row=0, column=0, padx=10)

code_text = scrolledtext.ScrolledText(input_frame, font="Times 15 bold", width=40, height=8, bg='black', fg='green')
code_text.grid(row=1, column=0, padx=10)

# Output frame
output_frame = tk.Frame(root, bg='black')
output_frame.pack(pady=10)

assembly_label = tk.Label(output_frame, text="Assembly code:", fg="white", bg="black")
assembly_label.grid(row=0, column=0, padx=10)

assembly_text = scrolledtext.ScrolledText(output_frame, width=80, height=40, bg='black', fg='green')
assembly_text.grid(row=1, column=0, padx=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_to_assembly, fg="white", bg="black")
convert_button.pack(pady=0)

root.mainloop()
