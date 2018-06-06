FROM rainu/browser-base:16.04  
MAINTAINER rainu <rainu@raysha.de>  
ENV DEBIAN_FRONTEND noninteractive  
  
#install Flash  
RUN echo "deb http://archive.canonical.com/ubuntu xenial partner" >>
/etc/apt/sources.list &&\  
apt-get update &&\  
apt-get -y install \  
adobe-flashplugin\  
libgl1-mesa-dri\  
libgl1-mesa-glx\  
libexif-dev\  
libv4l-0 &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#install chromium  
RUN apt-get update &&\  
apt-get -y install chromium-browser --no-install-recommends &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#create data-dir  
RUN mkdir /home/browser/.chromium &&\  
chown browser /home/browser/.chromium  
  
USER browser  
  
ENTRYPOINT ["/usr/bin/chromium-browser", "--user-data-
dir=/home/browser/.chromium"]  
CMD ["--no-sandbox"]  

