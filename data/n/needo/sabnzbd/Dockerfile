FROM phusion/baseimage:0.9.16  
MAINTAINER needo <needo@superhero.org>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
RUN add-apt-repository ppa:jcfp/ppa  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty
universe multiverse"  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-
updates universe multiverse"  
RUN add-apt-repository ppa:fnu/main-fnu  
RUN apt-get update -q  
RUN apt-get install -qy unrar par2 sabnzbdplus wget ffmpeg sabnzbdplus-theme-
mobile  
  
# Path to a directory that only contains the sabnzbd.conf  
VOLUME /config  
VOLUME /downloads  
  
EXPOSE 8080 9090  
# Add sabnzbd to runit  
RUN mkdir /etc/service/sabnzbd  
ADD sabnzbd.sh /etc/service/sabnzbd/run  
RUN chmod +x /etc/service/sabnzbd/run  

