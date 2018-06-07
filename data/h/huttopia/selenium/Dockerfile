FROM cedvan/ubuntu:14.04.20150311  
MAINTAINER dev@cedvan.com  
  
# Install java  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
openjdk-7-jre  
  
# Install simulator X-Server  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
xvfb  
  
# Install Firefox  
RUN wget
ftp://ftp.mozilla.org/pub/mozilla.org/firefox/releases/35.0/linux-x86_64/fr/firefox-35.0.tar.bz2
\  
&& tar -xjvf firefox-35.0.tar.bz2 \  
&& rm -rf /opt/firefox-* \  
&& mv firefox /opt/firefox-35.0 \  
&& ln -sf /opt/firefox-35.0/firefox /usr/bin/firefox  
  
# Install Chromium and ChromeDriver  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
chromium-browser  
  
# Install Opera  
RUN sh -c 'echo "deb http://deb.opera.com/opera/ stable non-free" >>
/etc/apt/sources.list.d/opera.list' \  
&& sh -c 'wget -O - http://deb.opera.com/archive.key | apt-key add -' \  
&& apt-get update -qq \  
&& apt-get install -qqy \  
opera  
  
# Remove useless list of packages  
RUN rm -rf /var/lib/apt/lists/*  
  
# Install Selenium  
ADD http://selenium-release.storage.googleapis.com/2.45/selenium-server-
standalone-2.45.0.jar /opt/selenium.jar  
  
# Install bin  
ADD assets/bin /bin/selenium  
RUN chmod +x /bin/selenium/*  
  
# Install drivers  
ADD assets/drivers /bin/selenium/drivers  
RUN chmod +x /bin/selenium/drivers/*  
  
EXPOSE 4444  
ENTRYPOINT ["/bin/selenium/init"]  

