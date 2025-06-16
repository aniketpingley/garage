import os
import base64


"""
generate_base64_html_pages.py

This script converts a series of PNG images (e.g., 1.png to N.png) into standalone HTML pages.
Each page embeds its corresponding image as a base64-encoded <img> tag, eliminating the need for external image files.
Navigation links ("Prev" and "Next") are included for sequential browsing, with styling applied for readability.

Usage:
- Place this script in a directory containing page-numbered PNG files (e.g., 1.png, 2.png, ..., 76.png).
- Run the script with Python 3.
- It will generate individual HTML files (1.html, 2.html, etc.) for each image.

Dependencies:
- Standard Python libraries only (no external packages required).

Output:
- Self-contained HTML files with embedded images and styled navigation links.
"""



def extract_number(filename):
    return int(os.path.splitext(filename)[0])  # Assumes filenames like '1.png'

# Get PNG files and sort naturally
image_files = sorted(
    [f for f in os.listdir() if f.endswith('.png')],
    key=extract_number
)

for i, img_file in enumerate(image_files):
    page_num = i + 1
    prev_page = f"{page_num - 1}.html" if i > 0 else None
    next_page = f"{page_num + 1}.html" if i < len(image_files) - 1 else None

    # Read and encode image to base64
    with open(img_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode('utf-8')
        data_uri = f"data:image/png;base64,{encoded_string}"

    # HTML template
    html = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  
  <style>
    body {{
      text-align: center;
      font-family: sans-serif;
      margin: 0;
      padding: 20px;
    }}
    .nav {{
      margin-top: 20px;
      font-size: 18px;
    }}
    .nav a {{
      color: #007BFF;
      text-decoration: none;
      margin: 0 10px;
      font-family: sans-serif;
    }}
    .nav a:hover {{
      text-decoration: underline;
    }}
    img {{
      width: 100%;
      max-width: 800px;
      margin-top: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
  </style>
</head>
<body>
  <h2>Page {page_num}</h2>
  <img src="{data_uri}" alt="Page {page_num}">
  <div class="nav">
    {'<a href="' + prev_page + '">Prev</a>' if prev_page else ''}
    {' | ' if prev_page and next_page else ''}
    {'<a href="' + next_page + '">Next</a>' if next_page else ''}
  </div>
</body>
</html>
'''

    with open(f"{page_num}.html", "w", encoding="utf-8") as f:
        f.write(html)
