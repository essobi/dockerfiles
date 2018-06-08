FROM library/java:8-jre  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Installing ffmpeg repo  
RUN curl http://www.deb-multimedia.org/pool/main/d/deb-multimedia-keyring/deb-
multimedia-keyring_2016.3.7_all.deb \  
-o /tmp/deb-multimedia-keyring_2016.3.7_all.deb && \  
dpkg -i /tmp/deb-multimedia-keyring_2016.3.7_all.deb && \  
rm /tmp/deb-multimedia-keyring_2016.3.7_all.deb  
  
RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >>
/etc/apt/sources.list && \  
echo "deb http://www.deb-multimedia.org jessie-backports main" >>
/etc/apt/sources.list  
  
# Installing Nodejs repo  
RUN curl
https://raw.githubusercontent.com/nodesource/distributions/master/deb/setup_4.x
-o /tmp/setup_4.x && bash /tmp/setup_4.x  
  
#Installing firefox repo and cleaning iceweasel  
RUN apt-get purge iceweasel icedove && echo "deb
http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all main" >
/etc/apt/sources.list.d/mozilla.list && \  
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C1289A29  
  
RUN apt-get update  
  
RUN apt-get install -y \  
xvfb \  
libgconf-2-4 \  
libexif12 \  
chromium \  
supervisor \  
netcat-traditional \  
x11vnc \  
ffmpeg \  
nodejs \  
firefox-mozilla-build libgtk-3-0  
  
# Installing http-backend-proxy through npm  
RUN npm install -g protractor http-backend-proxy  
  
# Install Selenium and Chrome driver  
RUN webdriver-manager update  
  
# Add a non-privileged user for running Protrator  
RUN adduser --home /project --uid 1100 \  
\--disabled-login --disabled-password --gecos node node  
  
# Add service defintions for Xvfb, VNC, Selenium and Protractor runner  
ADD supervisord/*.conf /etc/supervisor/conf.d/  
  
# By default, tests in /data directory will be executed once and then the
container  
# will quit. When MANUAL envorinment variable is set when starting the
container,  
# tests will NOT be executed and Xvfb and Selenium will keep running.  
ADD bin/run-protractor /usr/local/bin/run-protractor  
  
RUN chmod +x /usr/local/bin/run-protractor  
  
#Setting up x11vnc  
ENV DISPLAY_SIZE 1280x2200  
RUN npm install lodash moment jasmine-reporters  
RUN mkdir ~/.vnc  
# Setup a password  
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd  
  
# remove packages & listings to reduce image size  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Container's entry point, executing supervisord in the foreground  
CMD ["/usr/bin/supervisord", "-n"]  
  
# Protractor test project needs to be mounted at /project  
VOLUME ["/project"]  

