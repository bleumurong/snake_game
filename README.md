# Snake

A simple Snake game built with Python and Tkinter.

## Requirements

- Python 3 with Tkinter available
- Tkinter is included with many Python installations. On macOS, install Python from [python.org](https://www.python.org/downloads/) if your Python installation does not include Tkinter.

## Run the game

From this folder, create and activate a virtual environment:

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python snake_game.py
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python snake_game.py
```

Click the game window to start. Use the arrow keys to steer. After game over, click the window to play again.

## Upload to GitHub

1. Create a new, empty repository on [GitHub](https://github.com/new). Do not initialize it with a README, license, or `.gitignore`.
2. Open a terminal in this project folder and run:

   ```bash
   git init
   git add snake_game.py README.md .gitignore
   git commit -m "Add Snake game"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   git push -u origin main
   ```

3. Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with the GitHub username and repository name. GitHub may ask you to authenticate when you push.

If Git says your author identity is not configured, set it with your own details:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
