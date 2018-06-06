FROM ubuntu:14.04  
MAINTAINER Andy<mouyigang@gmail.com>  
  
#========================  
# Miscellaneous packages  
#========================  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
bzip2 \  
ca-certificates \  
sudo \  
unzip \  
wget \  
xvfb \  
fonts-takao-mincho fonts-takao ttf-indic-fonts \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#========================================  
# Add normal user with passwordless sudo  
#========================================  
RUN sudo useradd seluser --shell /bin/bash --create-home \  
&& sudo usermod -a -G sudo seluser \  
&& echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& echo 'seluser:secret' | chpasswd  
  
RUN mkdir -p /opt/selenium  
  
#==============================  
# Scripts to run Selenium Node  
#==============================  
COPY \  
entry_point.sh \  
functions.sh \  
/opt/bin/  
RUN chmod +x /opt/bin/entry_point.sh  
  
#============================  
# Some configuration options  
#============================  
ENV SCREEN_WIDTH 1360  
ENV SCREEN_HEIGHT 1020  
ENV SCREEN_DEPTH 24  
ENV DISPLAY :99.0  
#============================================  
# Google Chrome  
#============================================  
# can specify versions by CHROME_VERSION;  
# e.g. google-chrome-stable=53.0.2785.101-1  
# google-chrome-beta=53.0.2785.92-1  
# google-chrome-unstable=54.0.2840.14-1  
# latest (equivalent to google-chrome-stable)  
# google-chrome-beta (pull latest beta)  
#============================================  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install \  
${CHROME_VERSION:-google-chrome-stable} \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN apt-get update -qqy && apt-get install -y net-tools && rm -rf
/var/lib/apt/lists/* /var/cache/apt/*  
  
#=========  
# Firefox  
#=========  
ARG FIREFOX_VERSION=54.0.1  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install firefox \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& apt-get -y purge firefox \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox  
  
#=================================  
# Chrome Launch Script Modication  
#=================================  
COPY chrome_launcher.sh /opt/google/chrome/google-chrome  
RUN chmod +x /opt/google/chrome/google-chrome  
  
RUN chown -R seluser:seluser /opt/selenium  
  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
USER seluser  
CMD ["/opt/bin/entry_point.sh"]  

