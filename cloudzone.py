import subprocess
import ctypes
from typing import List

class CloudZone:
    def __init__(self):
        self.applications = ["Notepad", "Calculator", "Word", "Excel"]  # List of applications to adjust

    def get_display_settings(self) -> dict:
        """
        Retrieves the current display settings for the system.
        """
        try:
            process = subprocess.run(['reg', 'query', 'HKCU\\Control Panel\\Desktop'], capture_output=True, text=True)
            output = process.stdout
            settings = {}
            for line in output.splitlines():
                if ' ' in line:
                    key, value = line.strip().split('    ')
                    settings[key] = value
            return settings
        except Exception as e:
            print(f"Error retrieving display settings: {e}")
            return {}

    def adjust_settings_for_application(self, app_name: str):
        """
        Adjusts the display settings for a specific application.
        """
        settings = self.get_display_settings()
        print(f"Adjusting settings for {app_name}...")
        
        # Example adjustment: Check if scaling is set to 100% and adjust if necessary
        if 'LogPixels' in settings and settings['LogPixels'] != '96':
            print(f"Current DPI scaling for {app_name} is not optimal. Adjusting to 100%.")
            ctypes.windll.user32.SystemParametersInfoW(0x0073, 0, 96, 0)  # Adjust DPI scaling to 96 (100%)
        else:
            print(f"Settings for {app_name} are already optimized.")

    def adjust_all_applications(self):
        """
        Adjusts display settings for all predefined applications.
        """
        for app in self.applications:
            self.adjust_settings_for_application(app)

if __name__ == "__main__":
    cz = CloudZone()
    cz.adjust_all_applications()