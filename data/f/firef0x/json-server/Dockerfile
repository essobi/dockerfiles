FROM node:latest  
MAINTAINER Firef0x  
ENV PORT 3003  
ENV REFRESHED_AT 20160302173000  
RUN cd /opt \  
&& git clone https://github.com/Firef0x/json-server.git \  
&& cd /opt/json-server \  
&& npm install -g forever \  
&& npm install \  
&& chmod 755 /opt/json-server/run  
  
EXPOSE $PORT/tcp  
  
VOLUME ["/opt/json-server/db", "/opt/json-server/log"]  
WORKDIR /opt/json-server  
CMD ["/opt/json-server/run"]  

