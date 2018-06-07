FROM ubuntu:latest  
MAINTAINER zaolin <zaolin@das-labor.org>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y software-properties-common  
  
RUN add-apt-repository 'deb http://download.jitsi.org/nightly/deb unstable/'
&& \  
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C697D823EB0AB654 && \  
apt-get update && \  
apt-get -y install jitsi-meet && \  
apt-get clean  
  
EXPOSE 80 443  
CMD tail -F /var/log/messages  

