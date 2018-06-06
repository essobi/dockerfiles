FROM python:2.7  
MAINTAINER Zorex Salvo (zorexsalvo@gmail.com)  
  
COPY requirements.txt .  
RUN pip install -r requirements.txt  
  
COPY . /opt/  
WORKDIR /opt/  
  
EXPOSE 8000  
CMD ["./manage.py", "runserver" , "0.0.0.0:8000"]  

