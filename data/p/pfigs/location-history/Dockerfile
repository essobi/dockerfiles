FROM python:3  
WORKDIR /app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
CMD [ "python", "./parse_gmaps_lochist.py" ]  
  

