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
  
#install google chrome  
RUN apt-get update &&\  
apt-get -y install curl ca-certificates &&\  
curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add \-
&&\  
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list &&\  
apt-get update &&\  
apt-get install -y google-chrome-stable --no-install-recommends &&\  
apt-get purge --auto-remove -y curl &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#create data-dir  
RUN mkdir /home/browser/.chrome &&\  
chown browser /home/browser/.chrome  
  
USER browser  
  
ENTRYPOINT ["/usr/bin/google-chrome", "--no-first-run", "--user-data-
dir=/home/browser/.chrome"]  
CMD ["--no-sandbox"]  

