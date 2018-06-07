FROM openjdk:8-alpine  
  
MAINTAINER EstiNet  
  
ARG PORT_NUM  
ENV PORT_NUM ${PORT_NUM:-8102}  
  
ARG EC_PORT_NUM  
ENV EC_PORT_NUM ${EC_PORT_NUM:-6902}  
  
EXPOSE $EC_PORT_NUM $PORT_NUM  
  
COPY . /usr/src/server  
WORKDIR /usr/src/server  
  
RUN echo server-port=$PORT_NUM >> server.properties  
RUN echo port=$EC_PORT_NUM >> esticonsole.properties  
  
# RUN apk add --no-cache screen  
RUN mkdir /data  
RUN mkdir /data/logs  
RUN mkdir /data/plugins  
  
# CMD screen -S -X 'java -jar EstiConsole.jar\n'  
CMD exec java -jar EstiConsole.jar  

