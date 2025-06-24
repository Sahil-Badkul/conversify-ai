# conversify-ai

An LLM-powered conversational interface built with **Chainlit** and **OpenRouter API**, leveraging the **Mistral-7B-Instruct** model for interactive chat experiences.

## 🚀 Features

* ✅ Seamless interaction with powerful LLMs
* ✅ Conversation history management
* ✅ Extensible for further development or integration into apps
* ✅ Environment variable-based configuration for secure API management

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Sahil-Badkul/conversify-ai.git
cd conversify-ai

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

## ▶️ Usage

```bash
chainlit run main.py --port 8000
```

Then visit: [http://localhost:8000](http://localhost:8000)

## 🗂️ Project Structure

```
├── main.py            # Main application script
├── requirements.txt   # Python dependencies
├── .env               # Environment variables (Not committed to Git)
├── chainlit.md        # Welcome screen content for Chainlit
└── README.md          # Project documentation
```

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

## 🤝 Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
