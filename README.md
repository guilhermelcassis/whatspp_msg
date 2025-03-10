# Dunamis Greenhouse Messaging System

## Overview
The Dunamis Greenhouse Messaging System is a Python application designed to send personalized WhatsApp messages to students based on their preferred language. The application retrieves student data from Excel files and uses predefined message templates to communicate effectively.

## Features
- Send WhatsApp messages in multiple languages (English, Italian, Portuguese, French, Spanish, German).
- Automatically retrieve student data from Excel files.
- Use environment variables for configuration.
- Support for easy addition of new languages and message templates.

## Requirements
- Python 3.x
- Required Python packages:
  - `pywhatkit`
  - `pandas`
  - `python-dotenv`
  - `openpyxl` (for reading Excel files)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/guilhermelcassis/whatspp_msg.git
   cd whatspp_msg
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your Excel files in the `languages` directory. Ensure the files are named correctly (e.g., `english.xlsx`, `italian.xlsx`, etc.).
2. Run the messaging script:
   ```bash
   python send-msg.py
   ```

## File Structure
whatspp_msg/
│
├── languages/ # Directory containing Excel files
│ ├── english.xlsx
│ ├── italian.xlsx
│ ├── portuguese.xlsx
│ └── ... # Other language files
│
├── models.py # Student model definition
├── messages.py # Message templates for different languages
├── send-msg.py # Main script to send messages
├── .gitignore # Files and folders to ignore in Git
└── README.md # Project documentation


## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the Dunamis Greenhouse team for their support and guidance.
- Special thanks to the contributors who helped improve this project.