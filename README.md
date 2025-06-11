# Flask MTG Card finder
This website allows you to browse all MTG Cards available on the MTG API https://api.magicthegathering.io/v1/cards this project is a rewrite of my school project that was written in PHP it's now being rewritten to python

## Future Features 
- Simple Web-UI
- Docker Ready 

## To-Do list
- [❌] Create a Dockerfile
- [❌] Push the Image to DockerHub
- [❌] Show only the first 20 cards
- [❌] Finish the Website

## Installation (Local)

1. **Clone the repository**
```bash
git clone https://github.com/lilithbtw/mtg-flask.git
cd mtg-flask
```

2. **Create a virtual environment (recommended)**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Application**

```bash
python main.py
```

Then visit http://localhost:5000 in your browser.


## Building (Docker)

1. **Build the image**
```bash
docker build -t mtg-flask .
```

2. **Run the container**

```bash
docker run -p 80:5000 mtg-flask
```

Then visit http://localhost in your browser.

## Installation (Docker)

```bash
docker run -p 5000:5000 lilithbtw/mtg-flask
```

Then visit http://localhost:5000 in your browser