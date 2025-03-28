# 📌 Real-Time Image Detection Using TensorFlow  

This project performs **real-time image detection** using **TensorFlow**, a Flask backend, and a web-based frontend.  

## 🚀 Features  
✔️ Detects and recognizes objects via a webcam.  
✔️ Saves recognized objects in a JSON storage.  
✔️ Fully web-based frontend with HTML, CSS, and JavaScript.  
✔️ Backend powered by Flask and TensorFlow.  
✔️ Works on any device with dependencies installed.  

---

## **📥 Installation & Setup**  

### ✅ 1️⃣ Clone the Repository  
Run the following command in your terminal or command prompt:  

```sh
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
###✅ 2️⃣ Create a Virtual Environment
Since TensorFlow requires a proper environment, create a virtual environment to manage dependencies.
```sh
python -m venv venv

###✅ 3️⃣ Activate the Virtual Environment
Depending on your OS, activate the environment:

Windows (Command Prompt):

```sh
venv\Scripts\activate
Windows (PowerShell):

```sh
.\venv\Scripts\Activate
Mac/Linux:

```sh
source venv/bin/activate

###✅ 4️⃣ Install Dependencies
Install all required dependencies using:

```sh
pip install -r requirements.txt

###✅ 5️⃣ Run the Backend
Start the Flask backend server:

```sh
python app.py
It should display output like:

```nginx
Running on http://127.0.0.1:5000/

###✅ 6️⃣ Run the Frontend
Now, start a simple HTTP server for the frontend.

Navigate to the frontend folder:

```sh
cd frontend
Start the frontend server:

Using Python (Recommended):

```sh
python -m http.server 8000
Open http://localhost:8000 in your browser.

🛠️ Troubleshooting
❌ Issue: pip install -r requirements.txt fails.
✔️ Fix: Ensure Python & pip are updated.

❌ Issue: Webcam doesn’t open.
✔️ Fix: Check browser permissions.

❌ Issue: Flask doesn’t start.
✔️ Fix: Try:

```sh
flask run
❌ Issue: TensorFlow throws errors.
✔️ Fix: Use Python 3.8+ for compatibility.

##🤝 Contributing
Want to improve the project?
Feel free to fork the repo and submit a pull request! 🚀

##📜 License
This project is open-source and free to use.
