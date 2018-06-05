FROM debian:jessie  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-asterisk"  
LABEL version="latest"  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update --fix-missing && \  
apt-get update && \  
apt-get install -y -q asterisk asterisk-core-sounds-fr-wav curl  
  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD /start.sh  

