FROM jlesage/baseimage-gui:debian-8  
RUN \  
apt-get update -qy \  
&& apt-get install -qy \  
gsmartcontrol \  
&& apt-get clean \  
&& rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
COPY startapp.sh /startapp.sh  
ENV APP_NAME="GSmartControl" USER_ID=0 GROUP_ID=0 KEEP_APP_RUNNING=1  

