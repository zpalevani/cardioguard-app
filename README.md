🏥 Cardioguard App:
Cardioguard is a simple web application designed to calculate a Cardioguard Score based on patient details such as age, serum creatinine, ejection fraction, and serum sodium. This score helps assess risk factors and the need for close monitoring. This is an extension to my capstone 2 project accessible via my GitHub. 


🚀 Live Demo:
🔗 [Click for Live Demo](https://zarapalevani.com/cardiogaurd-score)

📌 Features:
 User-friendly form to input patient details
 Dynamic risk score calculation
 Hosted on Heroku for easy access
 Built using Flask, HTML/CSS, and Gunicorn

🛠️ Tech Stack:
Backend: Flask, Gunicorn
Frontend: HTML, CSS (Bootstrap)
Deployment: Heroku
Version Control: Git & GitHub


🚀 How to Run Locally:

1️⃣ Clone this repository

bash
Copy
Edit
git clone https://github.com/zpalevani/cardioguard-app.git
cd cardioguard-app

2️⃣ Create a virtual environment & activate it

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

3️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt

4️⃣ Run the app locally

bash
Copy
Edit
python app.py

5️⃣ Open your browser and go to http://127.0.0.1:5000/


🌍 Deploying to Heroku:

1️⃣ Login to Heroku

bash
Copy
Edit
heroku login

2️⃣ Create a Heroku app

bash
Copy
Edit
heroku create cardioguard-app

3️⃣ Add Heroku remote

bash
Copy
Edit
git remote add heroku https://git.heroku.com/cardioguard-app.git

4️⃣ Deploy to Heroku

bash
Copy
Edit
git push heroku main

5️⃣ Scale the dynos

bash
Copy
Edit
heroku ps:scale web=1

6️⃣ Open the app

bash
Copy
Edit
heroku open


📸 Screenshots:
TBC


📜 License:
This project is licensed under the MIT License.


💌 Acknowledgments:
Special thanks to the M2M team for inspiring me through this deployment journey! ❤️🚀
