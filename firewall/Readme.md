# Windows Firewall Rule Creation Script

This script allows you to easily create outbound firewall rules to block specific applications on your Windows computer. The list of applications to block is read from a text file called `block.txt`. For each application listed in `block.txt`, the script will create a new firewall rule that blocks outgoing traffic from the application.

## Prerequisites

- This script requires a Windows computer with the Windows Firewall enabled.
- Python 3 must be installed on the computer. You can download Python from the [official website](https://www.python.org/downloads/).

## Usage

1. Download the `firewall_block.py` file and save it to a location of your choice.

2. Open a command prompt window as an administrator.

   - Click the **Start** button and type **cmd** in the search box.
   - Right-click on **Command Prompt** and select **Run as administrator**.

3. Change to the directory containing the `firewall_block.py` file by running the following command:

   ```
   cd path\to\directory
   ```

   Replace `path\to\directory` with the actual path to the directory containing the `firewall_block.py` file.

4. Run the `firewall_block.py` script by running the following command:

   ```
   python firewall_block.py
   ```

   The script will automatically look for the `block.txt` file in the same directory as the script. If the `block.txt` file is located elsewhere, you can enter the file path when prompted.

   ```
   Enter the path to the blocklist file (default is ./block.txt):
   ```

5. The script will read the list of applications from `block.txt` and add a new outbound firewall rule for each application.

6. The specified applications in `block.txt` will now be blocked by the Windows Firewall. Any outgoing traffic from the applications will be blocked, preventing them from accessing the Internet.

## Customizing the `block.txt` file

The `block.txt` file contains a list of applications to be blocked by the Windows Firewall. Each application should be listed on a separate line. Lines that start with a `#` character are treated as comments and are ignored by the script.

Here's an example `block.txt` file with comments:

```
# Block web browsers
C:\Program Files\Mozilla Firefox\firefox.exe
C:\Program Files\Google\Chrome\Application\chrome.exe

# Block messaging apps
C:\Program Files\Microsoft Teams\current\Teams.exe
C:\Program Files\Slack\slack.exe
```

In this example, the script will block the Firefox and Chrome web browsers, as well as the Microsoft Teams and Slack messaging apps.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute it as you wish.