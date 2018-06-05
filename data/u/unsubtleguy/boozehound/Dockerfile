# BoozeHound docker image  
FROM ubuntu:latest  
MAINTAINER Matt "matt@c0refailure.com"  
RUN apt-get update  
RUN apt-get install -y python python-pip wget python-scrapy  
  
COPY . /home/  
  
WORKDIR /home  
RUN pip install -r requirements.txt  
ENTRYPOINT ["python"]  
CMD ["BoozeHound_UI/BoozeHound_UI.py"]  

