FROM python:3.6  
MAINTAINER William Turner <willtur.will@gmail.com>  
  
WORKDIR /usr/src/app  
  
COPY . .  
RUN pip install --no-cache-dir -r requirements.txt  
  
EXPOSE 8080/tcp  
  
CMD ["python3", "main.py"]  

