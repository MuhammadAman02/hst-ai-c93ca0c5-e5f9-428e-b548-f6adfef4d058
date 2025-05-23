# LinkedIn Landing Page Clone

A Python-native clone of the LinkedIn landing page built with NiceGUI.

## Features

- Responsive design that works on desktop and mobile
- Faithful recreation of LinkedIn's landing page UI
- Interactive elements with notifications
- Pure Python implementation with no JavaScript dependencies

## Screenshots

![LinkedIn Clone Screenshot](https://via.placeholder.com/800x450.png?text=LinkedIn+Clone+Screenshot)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/linkedin-clone.git
cd linkedin-clone
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the example:
```bash
cp .env.example .env
```

## Running the Application

Start the application with:

```bash
python main.py
```

The application will be available at http://localhost:8000

## Deployment

This application is ready to deploy on platforms like Fly.io:

1. Install the Fly CLI
2. Run `fly launch` to create a new app
3. Deploy with `fly deploy`

## Project Structure

```
linkedin-clone/
├── app/
│   ├── core/                # Core configuration
│   ├── frontend/            # Frontend implementation
│   │   └── nicegui_app.py   # NiceGUI application
│   ├── static/              # Static assets
│   └── templates/           # Templates (if needed)
├── main.py                  # Application entry point
├── requirements.txt         # Dependencies
├── .env                     # Environment variables
└── README.md                # Documentation
```

## Technologies Used

- [NiceGUI](https://nicegui.io/): Python-native UI framework
- [FastAPI](https://fastapi.tiangolo.com/): For API endpoints (if needed)
- [Uvicorn](https://www.uvicorn.org/): ASGI server

## License

MIT