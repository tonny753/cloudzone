# CloudZone

CloudZone is a Python program designed to fine-tune display settings for various applications on Windows to ensure optimal visual performance.

## Features

- Automatically adjusts display settings for a set of predefined applications.
- Ensures DPI scaling is optimal for each application.
- Can be extended to include more applications or different settings adjustments.

## Prerequisites

- Windows operating system
- Python 3.x installed
- Administrative privileges to modify system settings

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cloudzone.git
   ```

2. Navigate to the project directory:

   ```bash
   cd cloudzone
   ```

## Usage

Run the program using Python:

```bash
python cloudzone.py
```

This will adjust display settings for the predefined applications (Notepad, Calculator, Word, and Excel). You can modify the list of applications in the source code as needed.

## Customization

- To add more applications or change the settings being adjusted, edit the `applications` list and the logic within `adjust_settings_for_application` method in `cloudzone.py`.

## Disclaimer

This program modifies system settings, which may require administrative privileges. Use at your own risk and ensure you have proper backups of your system settings.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.