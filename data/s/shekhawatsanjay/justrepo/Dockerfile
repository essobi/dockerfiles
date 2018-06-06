FROM ubuntu  
  
#========================  
# Miscellaneous packages  
# iproute which is surprisingly not available in ubuntu:15.04 but is available
in ubuntu:latest  
# OpenJDK8  
# rlwrap is for azure-cli  
# groff is for aws-cli  
# tree is convenient for troubleshooting builds  
#========================  
RUN apt-get update -y \  
&& apt-get -y --no-install-recommends install \  
tar wget curl bzip2  
  
  
  
#=========  
# Firefox  
#=========  
ARG FIREFOX_VERSION=56.0  
  
# don't install firefox with apt-get because there are some problems,  
# install the binaries downloaded from mozilla  
# see https://github.com/SeleniumHQ/docker-
selenium/blob/3.0.1-fermium/NodeFirefox/Dockerfile#L13  
# workaround "D-Bus library appears to be incorrectly set up; failed to read
machine uuid"  
# run "dbus-uuidgen > /var/lib/dbus/machine-id"  
  
RUN apt-get update -y \  
&& wget -O /tmp/firefox.tar.bz2 http://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& tar -C /opt -xvjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
  
  
ENV SCREEN_WIDTH 1360  
ENV SCREEN_HEIGHT 1020  
ENV SCREEN_DEPTH 24  
ENV DISPLAY :99.0  
  

