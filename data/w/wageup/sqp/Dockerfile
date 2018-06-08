FROM python:3  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
EXPOSE 3306  
COPY . .  
  
CMD [ "python", "./run.py" ]  

