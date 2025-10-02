import requests

# === PDFShift API Key ===
API_KEY = "sk_ffa32ffd4ee07e875b62d3c74dc6e96cff450082"

# === Path to your HTML file ===
html_file_path = r"C:\Users\HP\Desktop\figma to html\A4-25-color.html"

# Read HTML content
with open(html_file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# PDFShift API endpoint
url = "https://api.pdfshift.io/v3/convert/pdf"

# Request body
payload = {
    "source": html_content,
    "landscape": False
}

# Headers
headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

# Send request
response = requests.post(url, json=payload, headers=headers)

# Save PDF if successful
if response.status_code == 200:
    output_path = r"C:\Users\HP\Desktop\figma to html\A4-25-color.pdf"
    with open(output_path, "wb") as f:
        f.write(response.content)
    print(f"✅ PDF created successfully: {output_path}")
else:
    print(f"❌ Error {response.status_code}: {response.text}")
