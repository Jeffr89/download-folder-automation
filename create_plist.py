import os

# The name of your launch agent
label = "com.user.downloadfolderautomation"

# Get the current directory assuming main.py is in the same directory as this script
current_dir = os.path.dirname(os.path.realpath(__file__))
main_py_path = os.path.join(current_dir, 'main.py')
python_path = '/usr/local/bin/python3'  # or use sys.executable for the current Python interpreter

# The content of the .plist file
plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{label}</string>
    
    <key>ProgramArguments</key>
    <array>
        <string>{python_path}</string>
        <string>{main_py_path}</string>
    </array>
    
    <key>StartCalendarInterval</key>
    <dict>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/tmp/{label}.stdout</string>

    <key>StandardErrorPath</key>
    <string>/tmp/{label}.stderr</string>

    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
"""

# Write the content to a file
plist_path = os.path.expanduser(f'~/Library/LaunchAgents/{label}.plist')
with open(plist_path, 'w') as plist_file:
    plist_file.write(plist_content)

print(f'.plist file created at: {plist_path}')