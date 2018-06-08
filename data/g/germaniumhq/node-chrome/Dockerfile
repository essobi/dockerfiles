FROM germaniumhq/base:2.0.6  
MAINTAINER Bogdan Mustiata <bogdan.mustiata@gmail.com>  
  
ENV REFRESHED_AT="2016.12.13-23:22:26"  
USER root  
  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy  
  
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
RUN apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable}  
  
#==================  
# Chrome webdriver  
#==================  
ARG CHROME_DRIVER_VERSION=2.30  
RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip
https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
\  
&& rm -rf /opt/germanium/chromedriver \  
&& unzip /tmp/chromedriver_linux64.zip -d /opt/germanium \  
&& rm /tmp/chromedriver_linux64.zip \  
&& mv /opt/germanium/chromedriver
/opt/germanium/chromedriver-$CHROME_DRIVER_VERSION \  
&& chmod 755 /opt/germanium/chromedriver-$CHROME_DRIVER_VERSION \  
&& ln -fs /opt/germanium/chromedriver-$CHROME_DRIVER_VERSION
/usr/bin/chromedriver  
  
#======================================  
# Install remoting apps.  
#======================================  
RUN apt-get install -y vnc4server \  
parcellite \  
novnc \  
websockify \  
psmisc \  
icewm \  
rxvt-unicode-256color  
  
#======================================  
# Cleanup of the packages.  
#======================================  
RUN rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
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
COPY chrome_launcher.sh /opt/google/chrome/google-chrome  
RUN chmod +x /opt/google/chrome/google-chrome  
  
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
  

