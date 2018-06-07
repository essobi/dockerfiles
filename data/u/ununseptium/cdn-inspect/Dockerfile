FROM python:3  
LABEL maintainer tim@arctium.io  
  
WORKDIR /usr/src/app  
  
COPY cdn-inspect/requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
CMD [ "python", "./cdn-inspect/app.py" ]

