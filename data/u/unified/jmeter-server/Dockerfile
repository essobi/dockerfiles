# DOCKER-VERSION 1.5.0  
FROM phusion/baseimage:0.9.17  
MAINTAINER Jethro Yu <jethro.yu@hopebaytech.com>  
  
ENV RMI_LOCALPORT=55501  
EXPOSE 1099 ${RMI_LOCALPORT}  
  
CMD ["/sbin/my_init"]  
RUN pwd  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN echo 'APT::Get::Clean=always;' >> /etc/apt/apt.conf.d/99AutomaticClean  
  
# Speed up apt with squid-deb-proxy on docker host  
RUN apt-get -qq update && \  
apt-get upgrade -y && \  
apt-get autoremove -y && \  
apt-get install -y openjdk-7-jre-headless wget unzip  
ENV DEBIAN_FRONTEND=  
  
ADD setup /tmp/setup  
RUN /tmp/setup/install_jmeter.sh  
ADD run /etc/service/jmeter-server/run  

