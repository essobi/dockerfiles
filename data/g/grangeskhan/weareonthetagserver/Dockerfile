FROM python:3.4.8-jessie  
WORKDIR /usr/src/app  
EXPOSE 8080  
CMD [ "./lazors.py" ]  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY lazors/ .

