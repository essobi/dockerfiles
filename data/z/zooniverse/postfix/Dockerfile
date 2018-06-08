FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y -q install postfix rsyslog ca-certificates  
  
EXPOSE 25  
  
ADD start.sh /  
  
ENTRYPOINT [ "/start.sh" ]  

