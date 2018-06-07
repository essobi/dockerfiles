FROM node  
  
EXPOSE 42024  
RUN curl -L https://github.com/docker/compose/releases/download/1.2.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
ADD entrypoint.sh /entrypoint.sh  
ADD server.js /server.js  
ADD package.json /package.json  
RUN npm install && \  
chmod +x /entrypoint.sh  
  
ADD lib /lib  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

