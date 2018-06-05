FROM ubuntu  
  
MAINTAINER bill@empowersecurityacademy.com  
  
RUN apt-get update  
  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential  
  
RUN apt-get install -y python python-dev python-distribute python-pip  
  
COPY . /src  
  
RUN cd /src; python setup.py install  
  
EXPOSE 8080  
CMD cd /src/main && python app.py

