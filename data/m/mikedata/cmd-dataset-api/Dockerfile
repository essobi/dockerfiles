  
FROM ubuntu:14.04  
MAINTAINER Michael Adams michael.adams@ons.gov.uk  
  
RUN apt-get -y update  
RUN apt-get -y install wget  
RUN wget
"https://raw.githubusercontent.com/MikeData/simpleFlask/master/app.py"  
  
RUN apt-get install -y python  
RUN apt-get install -y python-pip  
RUN pip install flask  
  
EXPOSE 5000  
ENTRYPOINT ["python"]  
CMD ["app.py"]

