# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
# NOTE: DO *NOT* EDIT THIS FILE. IT IS GENERATED.  
# PLEASE UPDATE Dockerfile.txt INSTEAD OF THIS FILE  
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
FROM selenium/node-chrome:3.7.1-beryllium  
LABEL authors=SeleniumHQ  
  
USER root  
  
#=====  
# VNC  
#=====  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
x11vnc \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#=================  
# Locale settings  
#=================  
ENV LANGUAGE zh_CN.UTF-8  
ENV LANG zh_CN.UTF-8  
RUN locale-gen zh_CN.UTF-8 \  
&& dpkg-reconfigure --frontend noninteractive locales \  
&& apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
language-pack-zh-han* \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
  
#=======  
# Fonts  
#=======  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
ttf-wqy-microhei \  
ttf-wqy-zenhei\  
xfonts-wqy\  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#=========  
# fluxbox  
# A fast, lightweight and responsive window manager  
#=========  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
fluxbox \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#=========timezone=============  
ENV TZ "Asia/Shanghai"  
RUN echo "${TZ}" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
  
USER seluser  
  
#==============================  
# Generating the VNC password as seluser  
# So the service can be started with seluser  
#==============================  
  
RUN mkdir -p ~/.vnc \  
&& x11vnc -storepasswd secret ~/.vnc/passwd  
  
#==============================  
# Scripts to run Selenium Node  
#==============================  
COPY entry_point.sh /opt/bin/entry_point.sh  
  
EXPOSE 5900  

