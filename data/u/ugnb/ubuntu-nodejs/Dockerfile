FROM phusion/baseimage  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get install -y git nodejs npm  
RUN ln -s "$(which nodejs)" /usr/bin/node  
RUN npm install -g forever  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80  
CMD cd /src && npm update && forever start /src/index.js && /sbin/my_init  

