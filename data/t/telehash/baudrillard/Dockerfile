# Baudrillard Dashboard  
FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -y python-software-properties python g++ make netcat-
traditional  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs  
RUN apt-get install -y python-pip  
  
ADD . /dashboard  
RUN cd /dashboard; pip install -r requirements.txt  

