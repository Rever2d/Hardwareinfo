import tkinter as tk
import subprocess
import os
from tkinter import filedialog
from tkinter import ttk
import configparser


class TerminalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("R-ansiblecontroller")
        root.geometry("720x950")
        self.servergroups = []
        self.file_path = ''
        self.extravars = ''

        # Load last used .ini file path from 'importantfile.txt'
        self.file_path = self.load_last_file_path()

        # Text widget to display terminal output
        self.output_text = tk.Text(self.root, wrap="word", height=40, width=80)
        self.output_text.pack(padx=10, pady=10)

        # Button to execute a command
        self.execute_button = tk.Button(self.root, text="Run Command", command=self.run_command)
        self.execute_button.pack(pady=10)

        # Button to change the .ini file
        self.change_playbook_button = tk.Button(self.root, text="Change .ini", command=self.change_playbook)
        self.change_playbook_button.pack(pady=10)

        # Button to update playbook list
        self.update_playbook_button = tk.Button(self.root, text="Update Playbooks", command=self.update_playbook_list)
        self.update_playbook_button.pack(pady=10)

        # Label and combobox for playbooks
        self.playbook_label = tk.Label(self.root, text="Select a playbook:")
        self.playbook_label.pack(pady=5)
        self.playbook_combo = ttk.Combobox(self.root, state="readonly")
        self.playbook_combo.pack(pady=10)
        self.playbook_combo.set("None Selected")

        # Label and combobox for server groups
        self.servergroup_label = tk.Label(self.root, text="Select a server group:")
        self.servergroup_label.pack(pady=5)
        self.servergroup_combo = ttk.Combobox(self.root, state="readonly")
        self.servergroup_combo.pack(pady=10)
        self.servergroup_combo.set("None Selected")

        # Label and Entry widget for extra vars
        self.extravars_label = tk.Label(self.root, text="Enter extra vars (e.g., var1=value1 var2=value2):")
        self.extravars_label.pack(pady=5)
        self.extravars_entry = tk.Entry(self.root, width=50)
        self.extravars_entry.pack(pady=10)
        self.extravars_entry.bind("<KeyRelease>", self.update_extravars)

        # Load initial server groups and playbooks
        self.load_server_groups()
        self.update_playbook_list()

    def load_last_file_path(self):
        try:
            with open("importantfile.txt", "r") as file:
                path = file.read().strip()
                if os.path.exists(path):
                    return path
        except FileNotFoundError:
            pass
        return ""  # Default to an empty string if no valid file path exists

    def load_server_groups(self):
        if not self.file_path:
            return

        config = configparser.ConfigParser(allow_no_value=True)
        config.read(self.file_path)

        # Get server groups excluding ':vars' sections
        self.servergroups = [section for section in config.sections() if not section.endswith(':vars')]

        # Update server group combobox
        self.servergroup_combo['values'] = self.servergroups
        self.servergroup_combo.set("None Selected")

    def update_extravars(self, event=None):
        """Update extravars whenever the user types in the Entry widget."""
        self.extravars = self.extravars_entry.get()

    def run_command(self):
        selected_playbook = self.playbook_combo.get()
        selected_servergroup = self.servergroup_combo.get()

        # Ensure a playbook is selected
        if selected_playbook == "None Selected":
            self.output_text.insert(tk.END, "Error: No playbook selected.\n")
            return

        # Build command string
        extravars_option = f"-e \"{self.extravars}\"" if self.extravars else ""
        servergroup_option = f"-l {selected_servergroup}" if selected_servergroup != "None Selected" else ""
        server_file =f'-i'
        command = f"ansible-playbook add_playbooks_here/{selected_playbook} {extravars_option} {servergroup_option}"
        print(command)
        # Run the command and display the output
        result = subprocess.run('ansible-playbook add_playbooks_here/hardwareinfo.yml', shell=True, capture_output=True, text=True)
        self.output_text.delete("1.0", tk.END)  # Clear previous output
        self.output_text.insert(tk.END, result.stdout)
        self.output_text.insert(tk.END, result.stderr)
        

    def update_playbook_list(self):
        playbook_dir = "add_playbooks_here"
        self.playbook_combo['values'] = []
        playbooks = [file for file in os.listdir('add_playbooks_here') if file.endswith(".yml")]
        self.playbook_combo['values'] = playbooks
        self.playbook_combo.set('none selected')

    def change_playbook(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("INI files", "*.ini")])
        if not self.file_path:
            return

        # Save the new file path for future use
        with open("importantfile.txt", "w") as file:
            file.write(self.file_path)

        # Reload server groups
        self.load_server_groups()


if __name__ == "__main__":
    root = tk.Tk()
    app = TerminalApp(root)
    root.mainloop()
