FROM python:3.4.3  
MAINTAINER Lukas Martinelli <me@lukasmartinelli.ch>  
  
WORKDIR /usr/src/app/  
COPY requirements.txt /usr/src/app/  
RUN pip install -r requirements.txt  
  
COPY . /usr/src/app/  
  
EXPOSE 8000  
CMD [ "./run_gunicorn.sh" ]  

