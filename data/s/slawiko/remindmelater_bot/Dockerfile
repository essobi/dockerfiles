FROM python:3.6-slim  
  
VOLUME /logs /store  
  
WORKDIR /app  
  
ADD . /app  
  
RUN pip install -r requirements.txt  
  
EXPOSE 80  
WORKDIR bot  
CMD ["python", "app.py"]

