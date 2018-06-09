FROM ubuntu:14.04  
MAINTAINER CC  
  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y wget apt-transport-https software-properties-common python
python-software-properties g++ make && \  
wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
&& \  
echo 'deb https://deb.nodesource.com/node precise main' >
/etc/apt/sources.list.d/nodesource.list && \  
echo 'deb-src https://deb.nodesource.com/node precise main' >>
/etc/apt/sources.list.d/nodesource.list && \  
apt-get update && \  
apt-get install -y nodejs && \  
apt-get purge -y wget apt-transport-https software-properties-common python
python-software-properties g++ make && \  
apt-get autoremove -y && \  
apt-get clean all  
  
ENV PATH $PATH:/nodejs/bin  
RUN node -v  
  
ENV TERM=xterm-color  
  
RUN apt-get update; \  
apt-get install -y \  
bison \  
build-essential \  
curl \  
flex \  
g++ \  
git \  
gperf \  
sqlite3 \  
libsqlite3-dev \  
fontconfig \  
libfontconfig1 \  
libfontconfig1-dev \  
libfreetype6 \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libpng-dev \  
libssl-dev \  
libqt5webkit5-dev \  
ruby \  
perl \  
unzip \  
wget \  
imagemagick && \  
npm install pm2 -g && \  
apt-get autoremove -y && \  
apt-get clean all  
  
RUN mkdir -p /usr/src; \  
cd /usr/src; \  
wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.0.0-source.zip; \  
unzip phantomjs-2.0.0-source.zip; \  
rm phantomjs-2.0.0-source.zip; \  
cd phantomjs-2.0.0; \  
./build.sh --confirm && \  
cp /usr/src/phantomjs-2.0.0/bin/phantomjs /usr/local/bin/phantomjs && \  
rm -r /usr/src/phantomjs-2.0.0/ && \  
rm -r /usr/share/  
  
ADD init.sh /init.sh  
  
RUN chmod 777 /init.sh  
  
EXPOSE 3000  
  
CMD ["sh","/init.sh"]

