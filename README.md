\# Mini AI Chatbot 🤖



A simple AI-powered chatbot website built using \*\*Python, Flask, HTML, CSS, JavaScript, and Google Gemini API\*\*.



This project allows users to enter questions and receive AI-generated responses through a clean and interactive chat interface.



\## 🚀 Features



\- Interactive chatbot interface

\- AI-generated responses using Google Gemini API

\- Flask backend for API communication

\- JavaScript Fetch API for sending messages

\- Asynchronous communication using `async/await`

\- Environment variables to protect API credentials

\- Responsive user interface



\## 🛠️ Technologies Used



| Technology | Purpose |

|---|---|

| Python | Backend programming |

| Flask | Web application framework |

| Google Gemini API | AI response generation |

| HTML5 | Website structure |

| CSS3 | Website styling |

| JavaScript | Chat functionality |

| Fetch API | Frontend-backend communication |

| python-dotenv | Loading environment variables |



\## 📁 Project Structure



```text

mini-ai-chatbot/

│

├── app.py

├── requirements.txt

├── .env

├── .env.example

├── .gitignore

│

├── templates/

│   └── index.html

│

└── static/

&#x20;   ├── style.css

&#x20;   └── script.js

```



\## ⚙️ Installation and Setup



\### Step 1: Clone the Repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



\### Step 2: Open the Project Folder



```bash

cd mini-ai-chatbot

```



\### Step 3: Create a Virtual Environment (Optional but Recommended)



```bash

python -m venv .venv

```



Activate it on Windows:



```powershell

.venv\\Scripts\\Activate

```



\### Step 4: Install Dependencies



```bash

pip install -r requirements.txt

```



\### Step 5: Configure the Gemini API Key



1\. Create an API key through \[Google AI Studio].

2\. Create a `.env` file in the project root.

3\. Add your API key:



```env

GEMINI\_API\_KEY=your\_actual\_api\_key

```



\*\*Security Note:\*\* Never upload your real `.env` file or API key to GitHub. The `.gitignore` file excludes `.env` from version control.



\### Step 6: Run the Flask Application



```bash

python app.py

```



Open your browser and visit:



```text

http://127.0.0.1:5000/

```



\## 🔄 How the Chatbot Works



1\. The user enters a message in the chatbot interface.

2\. JavaScript captures the message.

3\. The Fetch API sends the message to the Flask `/chat` endpoint.

4\. Flask receives the message using the POST request.

5\. The Gemini API processes the user's prompt.

6\. Gemini generates an AI response.

7\. Flask sends the response back as JSON.

8\. JavaScript displays the response in the chat interface.



\## 💻 Backend API Overview



The Flask application provides two main routes:



| Route | Method | Purpose |

|---|---|---|

| `/` | GET | Displays the chatbot homepage |

| `/chat` | POST | Processes user messages and returns AI responses |



\## 🔐 API Key Security



\- API credentials are stored in environment variables.

\- `python-dotenv` loads the credentials from `.env`.

\- `.gitignore` prevents `.env` from being committed.

\- `.env.example` provides a placeholder for configuration.



Never expose API credentials in frontend JavaScript or HTML files.



\## 📌 Future Improvements



\- Chat history management

\- Clear conversation option

\- Improved error handling

\- Chat loading indicator

\- Mobile-friendly interface

\- Deployment to a cloud hosting platform



\## 👨‍💻 Author



\*\*Praveen S\*\*



\- GitHub: \[Praveensri101](https://github.com/Praveensri101)

\- LinkedIn: \[Praveen S](https://www.linkedin.com/in/praveen-s-09839825a/)



\---



⭐ If you find this project useful, feel free to explore the repository!

