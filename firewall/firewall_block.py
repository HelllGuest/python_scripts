import os

# Get the path to the directory containing the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Look for the blocklist file in the script directory
blocklist_path = os.path.join(script_dir, "block.txt")
if not os.path.isfile(blocklist_path):
    # If the blocklist file isn't found in the script directory, prompt the user to enter the file path
    blocklist_path = input("Enter the path to the blocklist file: ")

# Read the list of applications from the blocklist file
with open(blocklist_path, "r") as f:
    blocklist = [line.strip() for line in f.readlines() if not line.startswith("#") and line.strip()]

# Add a firewall rule to block each application in the blocklist
for app in blocklist:
    rule_name = f"Block {app}"
    cmd = f"netsh advfirewall firewall add rule name=\"{rule_name}\" dir=out program=\"{app}\" action=block"
    os.system(cmd)
    print(f"Added firewall rule to block {app}")
