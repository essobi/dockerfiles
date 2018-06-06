FROM zennoe/steamcmd:latest  
MAINTAINER Thomas Schmitz <agrar.pfurtz@gmail.com>  
  
# Install dependcies  
USER root  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
jq \  
psmisc  
  
  
# switch to steam user  
USER steam  
  
# user options  
ENV QUERY_PORT=27015  
ENV TU_PORT=7777  
ENV AUTOUPDATE=false  
ENV AUTOINTERVAL=3600  
  
# add docker-entrypoint.sh and fix permissions  
COPY docker-entrypoint.sh /usr/local/bin/  
USER root  
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh && \  
mkdir /opt/tu  
  
USER steam  
  
  
VOLUME /opt/tu  
EXPOSE ${QUERY_PORT}/udp ${QUERY_PORT}/tcp ${TU_PORT}/udp 7778/udp 3478/udp
4379/udp 4380/udp  
  
# entrypoint  
ENTRYPOINT ["docker-entrypoint.sh"]  

