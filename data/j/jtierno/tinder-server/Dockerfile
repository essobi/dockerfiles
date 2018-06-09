  
####################################################  
## Dockerfile para el uso del Application Server ##  
## Basado en Ubuntu 15.10 ##  
####################################################  
  
# Imagen Ubuntu oficial versión 14.04  
FROM ubuntu:15.10  
  
MAINTAINER jtierno jtierno  
  
COPY ./ /home  
  
RUN cd /home && chmod 777 config.sh  
RUN cd /home && ./config.sh -test -dependencies  
WORKDIR /home/build  
CMD ["bash"]

