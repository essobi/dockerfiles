FROM ubuntu:14.04  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update && apt-get install -y \  
  
curl git libfontconfig  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
  
RUN apt-get update && apt-get install -y \  
  
nodejs  
  
RUN npm install -g cordova  
RUN npm install -g ionic  
  
RUN mkdir -p /usr/src  
  
COPY ./scripts/ /usr/src/scripts  
  
RUN chmod -R 755 /usr/src/scripts  
  
ENTRYPOINT ["/usr/src/scripts/start.sh"]  

