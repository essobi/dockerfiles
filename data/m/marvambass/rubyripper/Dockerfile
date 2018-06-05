FROM ubuntu:14.04  
MAINTAINER Marvin Winkler <marvambass@gmail.com>  
  
ENV DISPLAY :0  
ENV LANG C.UTF-8  
  
# install dependencies  
RUN apt-get update; apt-get install -y \  
wget \  
make \  
cd-discid \  
cdparanoia \  
cdrdao \  
flac \  
lame \  
mp3gain \  
normalize-audio \  
ruby-gnome2 \  
ruby \  
sox \  
vorbisgain \  
libcanberra-gtk-module  
  
# download rubyripper  
RUN wget "https://rubyripper.googlecode.com/files/rubyripper-0.6.2.tar.bz2"; \  
tar xvf rubyripper-*.tar.bz2; \  
mv rubyripper*/ rubyripper  
  
# add settings  
RUN mkdir -p /root/.config/rubyripper  
ADD settings /root/.config/rubyripper/settings  
  
# add rips dir  
RUN mkdir /rips  
  
CMD sleep 3 && chmod 777 -R /rips; cd /rubyripper/ && ./configure --enable-
gtk2 --enable-cli && make install && rrip_gui; chmod 777 -R /rips  

