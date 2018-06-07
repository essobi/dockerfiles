#Test Docker File for bottle  
FROM ubuntu:latest  
MAINTAINER filipe.d.lino@gmail.com  
  
RUN apt-get -y update && \  
apt-get install -y python python-dev python-pip python-virtualenv && \  
pip install stravalib bottle pymongo  
  
ADD . /app  
  
EXPOSE 80  
CMD ["python","/app/Strava/Bottle.py","&"]  

