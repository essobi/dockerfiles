FROM hurricane/dockergui:x11rdp  
MAINTAINER fresta  
  
ENV APP_NAME="SubtitleEdit" WIDTH=1280 HEIGHT=720 USER_ID=0 GROUP_ID=0
UMASK=0000  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update --quiet \  
&& apt-get install --quiet --yes mono-xsp4 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /SubtitleEdit \  
&& wget
https://github.com/SubtitleEdit/subtitleedit/releases/download/3.5.4/SE354.zip
\  
&& unzip -d /SubtitleEdit SE354.zip  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
EXPOSE 3389 8080  
COPY startapp.sh /  

