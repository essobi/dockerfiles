FROM ubuntu:14.04  
  
MAINTAINER tungshooter "tungshooter@gmail.com"  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y nodejs  
  
# needs this to find the nodejs exec  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN apt-get install -y npm  
RUN /usr/bin/npm install websocket  
  
EXPOSE 8080  
  
ENTRYPOINT ["/usr/bin/node", "/root/server.js"]  

