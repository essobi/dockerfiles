FROM ubuntu:16.04  
MAINTAINER Bogdan Mustiata <bogdan.mustiata@gmail.com>  
  
# this is actually the germanium-base  
#================================================  
# Customize sources for apt-get  
#================================================  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main universe\n" >
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu xenial-updates main universe\n"
>> /etc/apt/sources.list \  
&& echo "deb http://security.ubuntu.com/ubuntu xenial-security main
universe\n" >> /etc/apt/sources.list  
  
#========================  
# Miscellaneous packages  
# Includes minimal runtime used for executing non GUI Java programs  
#========================  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
bzip2 \  
ca-certificates \  
openjdk-8-jre-headless \  
sudo \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
  
#==========  
# Selenium  
#==========  
RUN mkdir -p /opt/germanium \  
&& wget --no-verbose https://selenium-
release.storage.googleapis.com/2.53/selenium-server-standalone-2.53.1.jar -O
/opt/germanium/selenium-server-standalone.jar  
  
#========================================  
# Add normal user with passwordless sudo  
#========================================  
RUN sudo useradd germanium --shell /bin/bash --create-home \  
&& sudo usermod -a -G sudo germanium \  
&& echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& echo 'germanium:secret' | chpasswd  
  
ENV REFRESHED_AT="2016.12.13-23:22:26"  
USER root  
  
#=========  
# Firefox  
#=========  
ARG FIREFOX_VERSION=47.0.1  
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
  
ENV PATH /opt/firefox:$PATH  
  
#============  
# GeckoDriver  
#============  
ARG GECKODRIVER_VERSION=0.11.1  
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz
https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-
linux64.tar.gz \  
&& rm -rf /opt/geckodriver \  
&& tar -C /opt -zxf /tmp/geckodriver.tar.gz \  
&& rm /tmp/geckodriver.tar.gz \  
&& mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \  
&& chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \  
&& ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver  
  
#======================================  
# Install remoting apps.  
#======================================  
RUN apt-get update -qqy \  
&& apt-get install -y vnc4server \  
parcellite \  
novnc \  
websockify \  
psmisc \  
icewm \  
rxvt-unicode-256color  
  
#======================================  
# Cleanup of the packages.  
#======================================  
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#========================  
# Selenium Configuration  
#========================  
ENV NODE_MAX_INSTANCES 1  
ENV NODE_MAX_SESSION 1  
ENV NODE_REGISTER_CYCLE 5000  
COPY generate_config /opt/germanium/generate_config  
RUN chmod +x /opt/germanium/generate_config  
  
#=================================  
# Chrome Launch Script Modication  
#=================================  
RUN chown -R germanium:germanium /opt/germanium  
  
USER germanium  
# Following line fixes  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
  
#======================================  
# Desktop UI Thingies  
#======================================  
ENV RUN_VNC_SERVER=1  
ENV VNC_SERVER_WIDTH=1024  
ENV VNC_SERVER_HEIGHT=768  
ENV VNC_SERVER_BPP=16  
ENV RUN_WEB_INTERFACE=0  
ENV RUN_ICEWM=1  
ENV VNC_PASSWORD=germanium  
  
ENV DISPLAY=:1  
RUN cp -R /usr/share/novnc /home/germanium/novnc && \  
mkdir -p /home/germanium/.icewm && \  
echo 'Theme="metal2/default.theme"' > /home/germanium/.icewm/theme && \  
mkdir -p /home/germanium/.vnc  
  
COPY bin/index.html /home/germanium/novnc/  
COPY bin/xstartup /home/germanium/.vnc/xstartup  
COPY bin/run-node.sh /home/germanium/bin/run-node.sh  
  
EXPOSE 5901  
EXPOSE 8081  
ENTRYPOINT /home/germanium/bin/run-node.sh  
  

