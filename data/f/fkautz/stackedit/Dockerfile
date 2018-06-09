FROM ubuntu  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get -y install git  
RUN apt-get -y install nodejs  
RUN apt-get -y install npm  
  
RUN git clone https://github.com/benweet/stackedit.git  
  
WORKDIR stackedit  
  
RUN npm install  
  
CMD nodejs server.js  
  
EXPOSE 3000  

