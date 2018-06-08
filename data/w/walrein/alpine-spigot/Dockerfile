FROM java:alpine  
MAINTAINER walrein  
  
RUN apk upgrade \--update && \  
apk add \--update --no-cache git openssl  
  
  
ENV SPIGOT_HOME /minecraft  
RUN mkdir ${SPIGOT_HOME}  
WORKDIR ${SPIGOT_HOME}  
ADD ./spigot_init.sh ${SPIGOT_HOME}/spigot_init.sh  
RUN chmod +x ${SPIGOT_HOME}/spigot_init.sh  
RUN ${SPIGOT_HOME}/spigot_init.sh  

