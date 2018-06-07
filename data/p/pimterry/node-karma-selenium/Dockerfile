FROM pimterry/node-karma  
MAINTAINER Tim Perry <pimterry@gmail.com>  
  
#================================================  
# Customize sources for apt-get  
#================================================  
RUN echo "deb http://archive.ubuntu.com/ubuntu vivid main universe" >
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu vivid-updates main universe" >>
/etc/apt/sources.list \  
&& apt-key adv \--keyserver keyserver.ubuntu.com \--recv-keys 40976EAF437D05B5
3B4FE6ACC0B21F32  
  
#========================  
# Miscellaneous packages  
# Includes minimal runtime used for executing non GUI Java programs  
#========================  
RUN apt-get update -y \  
&& apt-get -y \--no-install-recommends install \  
ca-certificates \  
openjdk-8-jre-headless \  
libxi6 \  
libgconf-2-4 \  
sudo \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i
's/securerandom\.source=file:\/dev\/random/securerandom\.source=file:\/dev\/urandom/'
./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
#==========  
# Selenium  
#==========  
RUN mkdir -p /opt/selenium \  
&& wget \--no-verbose http://selenium-
release.storage.googleapis.com/2.48/selenium-server-standalone-2.48.2.jar -O
/opt/selenium/selenium-server-standalone.jar  
#===================================  
# Download the latest Chrome driver  
#===================================  
ENV CHROME_DRIVER_VERSION 2.20  
RUN wget \--no-verbose -O /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
\  
&& rm -rf /opt/selenium/chromedriver \  
&& unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \  
&& rm /tmp/chromedriver_linux64.zip \  
&& mv /opt/selenium/chromedriver
/opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \  
&& chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \  
&& ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION
/usr/bin/chromedriver  
  
COPY start-selenium.sh /usr/local/bin/start-selenium  
RUN chmod +x /usr/local/bin/start-selenium  
  
EXPOSE 4444  

