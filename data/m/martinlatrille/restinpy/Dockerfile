FROM ubuntu  
MAINTAINER Martin Latrille <martin.amin.latrille@gmail.com>  
  
# Add the application resources URL  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main
universe" >> /etc/apt/sources.list  
  
# Update the sources list  
RUN apt-get update  
RUN apt-get install -y python python-dev python-distribute python-pip  
  
# App bootstrap  
ADD . /code  
WORKDIR /code  
  
RUN pip install -r requirements.txt  
  
EXPOSE 80  
CMD python src/restin.py runserver 80  

