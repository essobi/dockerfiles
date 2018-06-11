FROM wainox/pyload  
MAINTAINER Heiko Bornholdt "heiko@bornholdt.it"  
  
RUN apt-get update \  
&& \  
apt-get install -y \  
wget \  
openjdk-8-jre-headless \  
libmediainfo-dev \  
&& \  
apt-get clean \  
&& \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget
http://downloads.sourceforge.net/project/filebot/filebot/FileBot_4.7.9/filebot_4.7.9_amd64.deb
\  
&& \  
dpkg -i filebot_4.7.9_amd64.deb \  
&& \  
rm filebot_4.7.9_amd64.deb  

