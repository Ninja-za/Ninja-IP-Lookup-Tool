import tkinter as tk
import requests

root = tk.Tk()
root.title("NINJA IP LOOKUP")
root.geometry("280x350")
root.configure(bg="#111")




def save_ip():
    return entry.get()

def ip_lookup():

    ip = save_ip()
    
    url = f"https://ipwhois.app/json/{ip}"
    response = requests.get(url)
    data = response.json()
    
    output_box.delete("1.0", tk.END)
    
    output_box.insert(tk.END, f"Country: {data.get('country', 'N/A')}\n")
    output_box.insert(tk.END, f"Continent: {data.get('continent', 'N/A')}\n")
    output_box.insert(tk.END, f"Country Code: {data.get('country_code', 'N/A')}\n")
    output_box.insert(tk.END, f"Region: {data.get('region', 'N/A')}\n")
    output_box.insert(tk.END, f"City: {data.get('city', 'N/A')}\n")
    output_box.insert(tk.END, f"Timezone: {data.get('timezone', 'N/A')}\n")
    output_box.insert(tk.END, f"Latitude: {data.get('latitude', 'N/A')}\n")
    output_box.insert(tk.END, f"Longitude: {data.get('longitude', 'N/A')}\n")
    output_box.insert(tk.END, f"ISP: {data.get('isp', 'N/A')}\n")


label = tk.Label(root, text="NINJA IP LOOKUP",font=("Arial",20),fg="#8B00FF", bg="#111" )
label.pack()
label = tk.Label(root, text="ENTER IP:",fg="#6B00C2" ,bg="#111")
label.pack()

entry = tk.Entry(root, width=30, bg="#3A3A3A",fg="#8B00FF")
entry.pack(pady=5)


button = tk.Button(root, text="ENTER",bg="#8B00FF", command=ip_lookup)
button.pack(pady=5)

output_box = tk.Text(root, width=28, height=10, font=("Arial", 12), bg="#3A3A3A", fg="#8B00FF")
output_box.pack(pady=10)

root.mainloop()