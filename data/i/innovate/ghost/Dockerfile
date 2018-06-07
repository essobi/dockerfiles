FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get -y install wget unzip nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN mkdir /usr/local/ghost  
RUN wget https://ghost.org/zip/ghost-0.6.4.zip  
RUN unzip ghost-0.6.4.zip -d /usr/local/ghost  
RUN rm -f ghost-0.6.4.zip  
RUN cd /usr/local/ghost && npm install --production  
RUN mv /usr/local/ghost/config.example.js /usr/local/ghost/config.js  
RUN sed -i 's/127.0.0.1/0.0.0.0/g' /usr/local/ghost/config.js  
RUN sed -i 's/2368/80/g' /usr/local/ghost/config.js  
  
EXPOSE 80  
CMD cd /usr/local/ghost && npm start

