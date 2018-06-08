FROM linuxserver/baseimage  
MAINTAINER Uirel <uirel@gany.net>  
  
# Setup Mono Repo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF &&\  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo tee
/etc/apt/sources.list.d/mono-xamarin.list  
  
  
# Install Pre Requisites  
RUN add-apt-repository ppa:mc3man/trusty-media -y  
RUN apt-get -q update && \  
apt-get install -qy wget libopus0 opus-tools libopus-dev mono-devel unzip
ffmpeg rsync nano  
  
#Mappings and ports  
VOLUME ["/config"]  
  
#Clean Up  
RUN apt-get autoclean -y; apt-get autoremove -y &&\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Adding Custom files  
ADD init/ /etc/my_init.d/  
ADD services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh  

