rm ./dist ./build
pyinstaller --noconsole --onefile --add-data "logo.ico;." --icon="logo.ico" --name "reminder" reminder.py