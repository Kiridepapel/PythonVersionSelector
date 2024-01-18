import os
import subprocess
import tkinter as tk

class PythonVersionSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Version Selector")

        panel = tk.Frame(self)
        panel.pack()

        java_versions = self.find_java_versions()
        total_height = 0
        row = 0
        paddingY = 10

        for version, path in java_versions.items():
            button = tk.Button(panel, text=version, command=lambda p=path: self.set_java_home(p))
            pady = (paddingY if row == 0 else 0, paddingY)
            button.grid(row=row, column=0, pady=pady)
            total_height += button.winfo_reqheight() + sum(pady)
            row += 1

        self.geometry(f"300x{total_height}")
    
    def find_java_versions(self):
        java_versions = {}
        java_dir = "C:\\"
        for item in os.listdir(java_dir):
            item_path = os.path.join(java_dir, item)
            if os.path.isdir(item_path) and item.startswith("Python"):
                version = item[len("Python"):]
                if "0" not in version:
                    version = version[:1] + "." + version[1:]
                else:
                    version = version.replace("0", ".", 1)
                java_versions[f"Python {version}"] = item_path
        return java_versions

    def set_java_home(self, java_home_path):
        subprocess.run(["cmd.exe", "/c", "setx", "PYTHONHOME", f'{java_home_path}'])
        self.destroy()

if __name__ == '__main__':
    app = PythonVersionSelector()
    app.mainloop()
