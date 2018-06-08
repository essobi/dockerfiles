FROM selenium/node-firefox:2.47.1  
MAINTAINER Selenium <selenium-developers@googlegroups.com>  
  
USER root  
  
#=========  
# Firefox  
#=========  
RUN rm -f /opt/selenium/selenium-server-standalone.jar \  
&& wget --no-verbose https://selenium-
release.storage.googleapis.com/2.43/selenium-server-standalone-2.43.1.jar -O
/opt/selenium/selenium-server-standalone.jar  
  
RUN apt-get purge -qqy firefox  
  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
bzip2 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget
ftp.mozilla.org/pub/mozilla.org/firefox/releases/34.0.5/linux-x86_64/en-
US/firefox-34.0.5.tar.bz2 \  
&& tar -xjvf firefox-34.0.5.tar.bz2 \  
&& rm -rf /opt/firefox* \  
&& mv firefox /opt/firefox34.0.5 \  
&& ln -sf /opt/firefox34.0.5/firefox /usr/bin/firefox  
  
#=====  
# VNC  
#=====  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
x11vnc \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p ~/.vnc \  
&& x11vnc -storepasswd secret ~/.vnc/passwd  
  
#=================  
# Locale settings  
#=================  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure --frontend noninteractive locales \  
&& apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
language-pack-en \  
&& rm -rf /var/lib/apt/lists/*  
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
&& rm -rf /var/lib/apt/lists/*  
#=========  
# fluxbox  
# A fast, lightweight and responsive window manager  
#=========  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
fluxbox \  
&& rm -rf /var/lib/apt/lists/*  
#==============================  
# Scripts to run Selenium Node  
#==============================  
COPY entry_point.sh /opt/bin/entry_point.sh  
RUN chmod +x /opt/bin/entry_point.sh  
  
EXPOSE 5900  

