FROM ubuntu:precise  
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise universe" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y python-software-properties python g++ make redis-server
libicu-dev  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs  
RUN apt-get update  
  
copy . /src  
  
# Install app dependencies  
RUN cd src && npm install  
  
#EXPOSE 8080  
CMD ["node", "/src/app.js"]  

