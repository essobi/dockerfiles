FROM phusion/baseimage:0.9.16  
MAINTAINER needo <needo@superhero.org>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe
multiverse" && \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates
universe multiverse" && \  
apt-get update -q && \  
  
# Install Dependencies  
apt-get install -qy python python-cheetah ca-certificates wget unrar unzip &&
\  
  
# Install SickBeard  
mkdir /opt/sickbeard && \  
cd /tmp && \  
wget https://github.com/midgetspy/Sick-Beard/archive/master.zip && \  
unzip master.zip && \  
mv Sick-Beard-master/* /opt/sickbeard/ && \  
chown nobody:users /opt/sickbeard  
  
EXPOSE 8081  
# SickBeard Configuration  
VOLUME /config  
  
# Downloads directory  
VOLUME /downloads  
  
# TV directory  
VOLUME /tv  
  
# Add edge.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD edge.sh /etc/my_init.d/edge.sh  
RUN chmod +x /etc/my_init.d/edge.sh  
  
# Add Sickbeard to runit  
RUN mkdir /etc/service/sickbeard  
ADD sickbeard.sh /etc/service/sickbeard/run  
RUN chmod +x /etc/service/sickbeard/run  

