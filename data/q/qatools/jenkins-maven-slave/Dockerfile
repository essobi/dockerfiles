FROM qatools/jenkins-slave:latest  
  
MAINTAINER Eroshenko Artem  
  
# Install maven  
RUN \  
add-apt-repository ppa:andrei-pozolotin/maven3 && \  
apt-get update && \  
apt-get install -y -q --force-yes \--no-install-recommends maven3  
  
# Install PhantomJS  
ENV PHANTOMJS_VERSION 1.9.8  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y vim git wget libfreetype6 libfontconfig bzip2 && \  
mkdir -p /srv/var && \  
wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
apt-get autoremove -y && \  
apt-get clean all  

