# from django.shortcuts import render

# # Create your views here.

import os
from django.http import HttpResponse
from datetime import datetime
import pytz
import subprocess

def htop_view(request):
    # Get the required details
    full_name = "Anusha R"  
    username = os.getenv("USER", "unknown user")
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S.%f")
    
    # Get the 'top' output
    top_output = subprocess.getoutput('top -bn1')

    # Create the response HTML
    response_html = f"""
    <html>
    <body>
        <h2>HTop Information</h2>
        <p>Name: {full_name}</p>
        <p>Username: {username}</p>
        <p>Server Time (IST): {ist_time}</p>
        <pre>Top Output:\n{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response_html)
