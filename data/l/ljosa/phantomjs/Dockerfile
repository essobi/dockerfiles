FROM ubuntu:14.04  
#ADD phantomjs-2.1.1-linux-x86_64 /usr/local/phantomjs-2.1.1-linux-x86_64  
ADD
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
/usr/local/phantomjs-2.1.1-linux-x86_64  
RUN tar -C /usr/local -xjf /usr/local/phantomjs-2.1.1-linux-x86_64 && \  
cd /usr/local/bin; ln -s ../phantomjs-2.1.1-linux-x86_64/bin/* . && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
apt-add-repository multiverse && \  
add-apt-repository ppa:no1wantdthisname/ppa && \  
apt-get update && \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | sudo debconf-set-selections && \  
apt-get install -y wget libfontconfig libfreetype6 libfreetype6-dev ttf-
mscorefonts-installer fontconfig-infinality  
CMD phantomjs  
  

