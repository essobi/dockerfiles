FROM alpine:3.4  
MAINTAINER Matteo Crippa @ghego20  
  
ENV HOME /root  
ENV WORK_DIR /root/loopback  
ENV SCRIPT_PATH /root/loopback/bin/www  
  
# Set WORKDIR  
WORKDIR ${WORK_DIR}  
  
RUN apk add --no-cache git  
RUN apk add --no-cache nodejs  
RUN apk add --no-cache wget  
RUN apk add --no-cache vim  
RUN apk add --no-cache monit  
  
VOLUME ${WORK_DIR}  
  
RUN npm install -g strongloop  
RUN npm install -g nodemon  
  
COPY loopback.conf /etc/init/  
COPY monit-loopback.conf /etc/monit/conf-enabled  
  
CMD ["/usr/bin/monit", "-I"]  
CMD ${SCRIPT_PATH}  

