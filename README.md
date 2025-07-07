# ARYA-MOTO


ARYA-MOTO is a terminal-based Automobile Service Management System created in Python, designed with a focus on **ASCII aesthetics**, **modularity**, and **Linux CLI spirit**.  
It operates entirely from the terminal, making it lightweight, minimal, and perfect for retro hacker-style environments.

---

## 🧰 Features

- 📇 **Customer Registration**
- 🚗 **Vehicle Information Logging**
- 🛠️ **Service Entry Management**
- 📖 **View Service History**
- 💾 **Data Persistence with JSON**
- 🎨 **Beautiful CLI UI with Colors + ASCII Art**
- 💻 **Cross-platform (Linux & Windows)**

---

## 🖥️ Terminal Preview

```bash
╔════════════════════════════════════╗
║               MENU                ║
╚════════════════════════════════════╝

[1] Register Customer
[2] Add Vehicle
[3] Log Service Visit
[4] View All Service Records
[5] Exit

File structure
arya-moto/
├── main.py                    # Launcher & Main Menu
├── modules/
│   ├── customer.py            # Customer functions
│   ├── vehicle.py             # Vehicle handling
│   ├── service.py             # Service logging & history
├── data/
│   ├── customers.json         # Stored customer data
│   ├── vehicles.json          # Stored vehicle data
│   └── services.json          # Stored service logs
├── utils/                     # (Optional) UI or common functions
│   └── ui.py
├── brands.py                  # Branded pyfiglet banners
├── README.md

🐍 Requirements
Python 3.7+

pyfiglet package (optional, for ASCII banners)

bash
Copy
Edit

🔐 Why Terminal-Based?
This project was designed as a no-GUI challenge.
Where others might build a basic UI with Tkinter, ARYA-MOTO goes deeper, creating a full CLI experience with the feel of an elite black-ops dashboard.

▶️ Run the Project
python3 main.py

This project is modular. If you'd like to contribute:

Fork the repo

Create a new module (e.g., billing.py, inventory.py)

Follow the minimal ASCII + color UI style

Submit a Pull Request

