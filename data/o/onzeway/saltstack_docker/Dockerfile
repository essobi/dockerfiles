FROM debian:stable-slim  
  
RUN apt-get update -y  
RUN apt-get install -y curl  
  
ENV SALT_VERSION 2016.11.0  
RUN cd /tmp && curl -L https://bootstrap.saltstack.com -o install_salt.sh  
RUN /bin/bash /tmp/install_salt.sh -M -P -N -X stable ${SALT_VERSION}  
  
EXPOSE 4505 4506  
CMD salt-master  

