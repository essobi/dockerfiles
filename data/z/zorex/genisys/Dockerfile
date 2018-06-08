FROM python:2.7  
MAINTAINER Zorex Salvo (zorexsalvo@gmail.com)  
  
RUN apt-get update  
  
COPY requirements.txt /opt/  
  
RUN pip install -r /opt/requirements.txt  
  
COPY . /opt/  
WORKDIR /opt/  
  
EXPOSE 8000  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  

