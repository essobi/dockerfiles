FROM openjdk:7-jre-alpine  
  
RUN apk add --update mongodb  
ADD https://dl.ubnt.com/mfi/2.1.11/mFi.unix.zip /  
RUN unzip mFi.unix.zip && rm mFi.unix.zip  
RUN mkdir -p /mFi/logs && ln -s /dev/stderr /mFi/logs/mongod.log && ln -s
/dev/stderr /mFi/logs/server.log  
RUN rm /mFi/bin/mongod && ln -s /usr/bin/mongod /mFi/bin/mongod  
  
EXPOSE 6843/tcp 6080/tcp 6880/tcp 6443/tcp 2323/tcp  
EXPOSE 10001/udp 3478/udp 1900/udp  
  
WORKDIR /mFi  
  
CMD ["java", "-jar", "lib/ace.jar", "start"]  

