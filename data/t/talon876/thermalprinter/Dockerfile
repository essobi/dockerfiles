FROM talon876/python:web  
MAINTAINER talondaniels@gmail.com  
  
WORKDIR /app  
  
COPY . /app  
  
RUN pip install -U -r requirements.txt && mkdir /app/tmp  
  
CMD ["python", "/app/runp.py"]  
  

