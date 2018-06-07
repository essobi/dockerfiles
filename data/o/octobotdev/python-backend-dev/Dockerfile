FROM python:3.6  
LABEL maintainer "jsaavedra@octobot.io"  
  
RUN pip3 install --upgrade pip  
  
VOLUME ["/usr/development/app","/usr/development/media"]  
WORKDIR /usr/development/app  
  
# You need to run this whenever you use this image as base for another  
# COPY requirements.txt /usr/development/  
# RUN pip3 install -r /usr/development/requirements.txt  
EXPOSE 8000  
# You should set the DJANGO_SETTINGS_MODULE to the appropiate django file  
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]  

