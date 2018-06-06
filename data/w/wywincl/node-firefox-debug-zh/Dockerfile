# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
# NOTE: DO *NOT* EDIT THIS FILE. IT IS GENERATED.  
# PLEASE UPDATE Dockerfile.txt INSTEAD OF THIS FILE  
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
FROM wywincl/node-firefox:latest  
MAINTAINER wywincl <wywincl@126.com>  
  
USER root  
  
#=====  
# VNC  
#=====  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
x11vnc \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& mkdir -p /root/.vnc \  
&& x11vnc -storepasswd secret ~/.vnc/passwd  
  
#=================  
# Locale settings  
#=================  
ENV LANGUAGE zh_CN.UTF-8  
ENV LANG zh_CN.UTF-8  
RUN locale-gen zh_CN.UTF-8 \  
&& dpkg-reconfigure --frontend noninteractive locales \  
&& apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
language-pack-zh-hans \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#=======  
# Fonts  
#=======  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
fonts-ipafont-gothic \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
xfonts-scalable \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#=========  
# fluxbox  
# A fast, lightweight and responsive window manager  
#=========  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
fluxbox \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#==============================  
# Scripts to run Selenium Node  
#==============================  
COPY entry_point.sh /opt/bin/entry_point.sh  
RUN chmod +x /opt/bin/entry_point.sh  
  
EXPOSE 5900  

