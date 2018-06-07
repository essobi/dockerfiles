FROM python:2.7  
MAINTAINER @x110dc  
  
COPY requirements.txt /app/  
RUN pip install -r /app/requirements.txt  
  
COPY *.py /app/  
ENTRYPOINT ["python", "/app/walls.py"]  

