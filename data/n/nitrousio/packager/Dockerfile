From ubuntu:14.04  
MAINTAINER Nitrous.IO <eng@nitrous.io>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
libxml2-dev \  
curl \  
git-core \  
ruby1.9.3 \  
ruby1.9.1-dev \  
libssl-dev \  
python-dateutil \  
wget \  
unzip  
  
# Install fpm  
RUN gem install fpm --version 1.2.0 --no-ri --no-rdoc  
  
# Install deb-s3  
RUN gem install deb-s3 --version 0.6.2 --no-ri --no-rdoc  
  
# Setup repos  
RUN mkdir -p /apt.nitrous.io/cache  
RUN mkdir -p /apt.nitrous.io/lib  
RUN mkdir -p /apt.nitrous.io/.gpg  
  
# Required for:
https://github.com/krobertson/deb-s3/issues/39#issuecomment-48723706  
ADD files/10-tcp.conf /etc/sysctl.d/10-tcp.conf  
  
# Utility binary which is a wrapper around deb-s3  
ADD files/deb-upload /usr/bin/deb-upload  
  
RUN chmod +x /usr/bin/deb-upload  
  
# Install xar  
RUN curl -s https://xar.googlecode.com/files/xar-1.5.2.tar.gz \  
| tar -v -C /root -xz && \  
cd /root/xar-1.5.2 && \  
./configure && \  
make && \  
make install && \  
rm -rf /root/xar-1.5.2  
  
# Install bom  
RUN curl -L -s https://github.com/hogliux/bomutils/archive/0.2.tar.gz \  
| tar -v -C /root -zx && \  
cd /root/bomutils-0.2 && \  
make && \  
make install && \  
rm -rf /root/bomutils-0.2  
  
# Install s3cmd  
RUN curl -L -s https://github.com/s3tools/s3cmd/archive/v1.5.0-rc1.tar.gz \  
| tar -v -C /root -xz && \  
cd /root/s3cmd-1.5.0-rc1 && \  
python setup.py install && \  
rm -rf /root/s3cmd-1.5.0-rc1  
  
# Install packer  
RUN wget https://dl.bintray.com/mitchellh/packer/0.6.1_linux_amd64.zip -O
/tmp/packer.zip; \  
unzip -d /usr/local/bin /tmp/packer.zip; \  
rm /tmp/packer.zip  

