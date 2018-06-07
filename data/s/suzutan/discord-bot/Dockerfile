FROM python:3  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install -r requirements.txt  
COPY core core  
COPY app.py .  
  
CMD ["python", "app.py"]  
  

