FROM ubuntu:14.04  
MAINTAINER chrodriguez <chrodriguez@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
# Don't ask user options when installing  
env DEBIAN_FRONTEND noninteractive  
RUN echo APT::Install-Recommends "0"; >> /etc/apt/apt.conf  
RUN echo APT::Install-Suggests "0"; >> /etc/apt/apt.conf  
  
# Update system  
RUN apt-get -y update && apt-get -y dist-upgrade && \  
apt-get install -y python-cheetah git software-properties-common \  
python-software-properties && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu precise
multiverse" && \  
apt-get -y update && apt-get install unrar  
  
RUN apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
VOLUME ["/sickrage", "/shows"]  
  
EXPOSE 8081  
ENTRYPOINT ["/entrypoint.sh"]  
  

