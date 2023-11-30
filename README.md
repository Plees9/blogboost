# Blogger auto post tool
Use chatgpt api to genarate content and post to blogger.

## Installation
Create virtual eviroment.
```bash
python -m venv .venv
```
activate .venv

```bash
.venv\Scripts\acvivate
```

Use the package manage [pip] to install.

```bash
pip install -r requirement.txt
```
## Usage
1. Get your own API key from ChatGPT (https://beta.openai.com/docs/api-reference)
2. Set up a new project in Google Cloud Platform, enable APIs for Google Sheets V4 and Google Drive API v3.
3. Create a service account with permissions: "Service Account Token Creator" on Google Sheets API and "Editor" on Google Drive API.
4. Create a service account with "Editor" role on both projects. Download JSON file as `credentials.json`.
5. Run script:
  python main.py
