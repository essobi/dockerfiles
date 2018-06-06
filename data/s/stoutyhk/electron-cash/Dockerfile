FROM ubuntu:xenial  
MAINTAINER Michal Belica <devel@beli.sk>  
EXPOSE 10000  
  
# runs as UID 1000 GID 1000 inside the container  
# heavily inspired by https://hub.docker.com/r/beli/electrum/  
  
ENV VERSION 2.9.3  
  
#temp while https://raw.githubusercontent.com/fyookball/keys-n-hashes is down  
COPY Electron-Cash-2.9.3.tar.gz.txt /tmp/Electron-Cash-2.9.3.tar.gz.txt  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
curl xpra python-qt4 python-pip python-setuptools lzop liblz4-tool sudo \  
&& curl -o /tmp/Electron-Cash-${VERSION}.tar.gz
https://electroncash.org/downloads/${VERSION}/win-linux/Electron-
Cash-${VERSION}.tar.gz \  
# temp while https://raw.githubusercontent.com/fyookball/keys-n-hashes is down  
#&& curl -o /tmp/Electron-Cash-${VERSION}.tar.gz.txt
https://raw.githubusercontent.com/fyookball/keys-n-hashes/master/sigs-and-
sums/${VERSION}/win-linux/SHA1.Electron-Cash-${VERSION}.tar.gz.txt \  
&& cd /tmp \  
&& mkdir .X11-unix \  
&& sha1sum Electron-Cash-${VERSION}.tar.gz > /tmp/Electron-Cash-${VERSION}.txt
\  
&& diff Electron-Cash-${VERSION}.txt Electron-Cash-${VERSION}.tar.gz.txt \  
&& pip install \--upgrade pip \  
&& pip install wheel \  
&& pip install cython \  
&& pip install rencode \  
&& pip install /tmp/Electron-Cash-${VERSION}.tar.gz \  
&& test -f /usr/local/bin/electron-cash \  
&& rm -vrf /tmp/Electron-Cash-${VERSION}.tar.gz /tmp/Electron-
Cash-${VERSION}.tar.gz.txt /tmp/Electron-Cash-${VERSION}.txt \  
&& apt-get purge \--autoremove -y python-pip python-setuptools curl \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# disable starting of other programs in default xpra.conf  
RUN sed -ie 's/^start-child/#start-child/' /etc/xpra/xpra.conf  
  
RUN useradd -d /home/user -m user \  
&& mkdir /electron-cash \  
&& ln -s /electron-cash /home/user/.electron-cash \  
&& chown user:user /electron-cash \  
&& chmod 777 -R /electron-cash \  
&& chown root:root /tmp/.X11-unix \  
&& chmod 777 -R /tmp/.X11-unix  
USER user  
ENV HOME /home/user  
WORKDIR /home/user  
VOLUME /electron-cash  
  
CMD ["/usr/bin/xpra", "start", ":100", "--compressors=lz4", "--start-
child=/usr/local/bin/electron-cash", "--bind-tcp=0.0.0.0:10000", "--no-
daemon", "--no-notifications", "--no-mdns", "--no-pulseaudio", "--exit-with-
children"]  

