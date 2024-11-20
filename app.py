import tkinter as tk
from tkinter import filedialog
import pywhatkit as kit
import time

def send_message():
    phone_numbers = entry_numbers.get().split(',')
    message = entry_message.get("1.0", tk.END).strip()
    image_path = entry_image.get().strip()

    for phone_no in phone_numbers:
        phone_no = phone_no.strip()
        if message:
            kit.sendwhatmsg_instantly(phone_no, message, wait_time=200, tab_close=True)
            time.sleep(200) 
        if image_path:
            kit.sendwhats_image(phone_no, image_path, wait_time=200, tab_close=True)
            time.sleep(200) 

    label_status.config(text="Mensagens enviadas com sucesso!")

def browse_image():
    file_path = filedialog.askopenfilename()
    entry_image.delete(0, tk.END)
    entry_image.insert(0, file_path)

# Criação da interface gráfica com tkinter
app = tk.Tk()
app.title("Envio de Mensagens WhatsApp")
app.geometry("1400x600")

frame = tk.Frame(app)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

font_style = ("Arial", 12)

tk.Label(frame, text="Números de WhatsApp (separados por vírgula):", font=font_style).pack(pady=5)
entry_numbers = tk.Entry(frame, width=50, font=font_style)
entry_numbers.pack(pady=5)

tk.Label(frame, text="Mensagem:", font=font_style).pack(pady=5)
entry_message = tk.Text(frame, height=10, width=50, font=font_style)
entry_message.pack(pady=5)

tk.Label(frame, text="Caminho da Imagem:", font=font_style).pack(pady=5)
entry_image = tk.Entry(frame, width=50, font=font_style)
entry_image.pack(pady=5)
tk.Button(frame, text="Procurar", command=browse_image, font=font_style).pack(pady=5)

tk.Button(frame, text="Enviar", command=send_message, font=font_style).pack(pady=5)
label_status = tk.Label(frame, text="", font=font_style)
label_status.pack(pady=5)

app.mainloop()