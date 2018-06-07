FROM ubuntu:14.04.4  
  
RUN apt-get update && apt-get install -y git-core \  
curl zlib1g-dev build-essential \  
libssl-dev libreadline-dev \  
libyaml-dev libsqlite3-dev \  
sqlite3 libxml2-dev libxslt1-dev \  
libcurl4-openssl-dev python-software-properties \  
libffi-dev libpq-dev qtbase5-dev \  
xvfb xserver-xorg-video-dummy \  
libyaml-dev libncurses5-dev libffi-dev \  
libgdbm3 libgdbm-dev mesa-common-dev \  
libgd-dev libgl1-mesa-dev  
WORKDIR /root  
  
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz && \  
tar -xzvf ruby-2.3.1.tar.gz && \  
cd ruby-2.3.1/ && \  
./configure && \  
make && make install && \  
rm -rf /root/ruby-2.3.1/  
  
  
RUN curl -O https://dl.dropboxusercontent.com/u/10287287/Packages/qt-5.5.1.deb
&& \  
dpkg -i qt-5.5.1.deb && \  
rm /root/qt-5.5.1.deb  
  
  
RUN apt-get purge build-essential -y && \  
apt-get clean && \  
rm -rf /tmp/*  
  
ADD config/xorg.conf /etc/X11/xorg.conf  
ADD config/xorg /etc/init.d/xorg  

