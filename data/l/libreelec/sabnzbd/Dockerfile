FROM libreelec/python:1.0.1  
MAINTAINER docker@libreelec.tv  
  
RUN apk add \--update autoconf \  
automake \  
g++ \  
gcc \  
make \  
p7zip \  
unrar \  
unzip \  
python-dev \  
&& wget -O - https://github.com/Parchive/par2cmdline/archive/v0.6.13.tar.gz |
tar xzf - -C /root \  
&& cd /root/par2cmdline-0.6.13 \  
&& aclocal \  
&& automake \--add-missing \  
&& autoconf \  
&& ./configure \  
&& make install \  
&& cd / \  
&& wget -O - http://www.golug.it/pub/yenc/yenc-0.4.0.tar.gz | tar xzf - -C
/root \  
&& cd /root/yenc-0.4.0 \  
&& python setup.py build \  
&& python setup.py install \  
&& cd / \  
&& wget -O - https://github.com/sabnzbd/sabnzbd/archive/1.0.1.tar.gz | tar xzf
- \  
&& mv /sabnzbd-1.0.1 /sabnzbd \  
&& cd /sabnzbd \  
&& apk del \--purge autoconf \  
automake \  
g++ \  
gcc \  
make \  
python-dev \  
&& rm -rf /root/par2cmdline* \  
&& rm -rf /root/yenc* \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*  
  
EXPOSE 8080  
  
VOLUME ["/config", "/data"]  
  
# SABnzbd will store it's configuration in ~/.sabnzbd  
ENV HOME /config  
  
CMD ["/usr/bin/python", "/sabnzbd/SABnzbd.py", "--config-file", "/config", "--
console","--server", "0.0.0.0:8080", "--browser", "0"]  

