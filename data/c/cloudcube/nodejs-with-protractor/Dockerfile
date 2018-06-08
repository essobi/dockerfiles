FROM cloudcube/nodejs:4.x  
MAINTAINER "zhaohaibin@outlook.com"  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
  
# prepare java && firefox source file  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get update && \  
apt-get install -y -q software-properties-common \  
wget \  
curl && \  
add-apt-repository -y ppa:webupd8team/java && \  
add-apt-repository -y ppa:mozillateam/firefox-next && \  
apt-get update -y  
  
# ffmpeg is hosted at deb-multimedia.org  
RUN \  
curl https://www.deb-multimedia.org/pool/main/d/deb-multimedia-keyring/deb-
multimedia-keyring_2016.3.7_all.deb -o /tmp/deb-multimedia-
keyring_2015.6.1_all.deb && \  
dpkg -i /tmp/deb-multimedia-keyring_2015.6.1_all.deb && \  
rm /tmp/deb-multimedia-keyring_2015.6.1_all.deb && \  
echo "deb http://www.deb-multimedia.org stretch main non-free" >>
/etc/apt/sources.list.d/multimedia.list  
  
# prepare google source file  
RUN \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add -  
RUN \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list  
RUN \  
apt-get update -y  
  
# install dependence software  
RUN \  
apt-get install -y -q \  
firefox \  
google-chrome-beta \  
x11vnc \  
oracle-java8-installer \  
xvfb \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-scalable \  
xfonts-cyrillic \  
libgconf-2-4 \  
libexif12 \  
netcat-traditional && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# add seleuser  
RUN \  
useradd -d /home/seleuser -m seleuser  
RUN \  
mkdir -p /home/seleuser/chrome  
RUN \  
chown -R seleuser /home/seleuser  
RUN \  
chgrp -R seleuser /home/seleuser  
  
# add startup scripts  
ADD ./scripts/ /home/root/scripts  
  
# install protractor selenium-standalone selenium-standalone  
RUN \  
npm install -g \  
protractor \  
selenium-standalone \  
phantomjs-prebuilt && \  
selenium-standalone install  
  
# update webdriver  
RUN \  
webdriver-manager update  
  
# export port 22 and 3000  
EXPOSE 22 3000 4444 5999  
ENTRYPOINT ["sh", "/home/root/scripts/start.sh"]  

