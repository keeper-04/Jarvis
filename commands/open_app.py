apps = {
    "opera": "C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Opera browser.lnk",
    "notepad": "C:\\Windows\\System32\\notepad.exe",
    "calculator": "C:\\Windows\\System32\\calc.exe"
}

def run(app_name):
    app_name = app_name.lower().strip()
    if app_name in apps:
        import os
        os.startfile(apps[app_name])
        return f"Opening {app_name}..."
    else:
        return f"Sorry, I don't know how to open {app_name}."