FROM python:3.5.2  
ADD requirements.txt /app/  
  
WORKDIR /app/  
  
RUN pip install -r requirements.txt  
  
ADD app.py /app/  
  
EXPOSE 8080  
CMD ["python", "app.py"]

