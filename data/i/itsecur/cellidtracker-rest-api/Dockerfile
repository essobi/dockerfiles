FROM python:3.6.4  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY cellidtracker_rest_api.py ./  
  
CMD [ "gunicorn", "-b", "0.0.0.0:5000", "--preload",
"cellidtracker_rest_api:app" ]

