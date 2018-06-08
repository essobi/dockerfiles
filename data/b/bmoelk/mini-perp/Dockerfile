FROM mini/base  
MAINTAINER Brian Moelk <bmoelk@gmail.com>  
  
# install perp  
RUN cd /root && \  
apk-install gcc make libc-dev && \  
/usr/bin/wget \--quiet \--output-document=/root/perp-2.07.tar.gz
http://b0llix.net/perp/distfiles/perp-2.07.tar.gz && \  
/bin/echo '2d2f24fc45a405876f101701ab8059f5ac7ad07a perp-2.07.tar.gz' >
perp-2.07.sha1 && /usr/bin/sha1sum -c perp-2.07.sha1 && \  
/bin/tar \--directory=/root -zxf /root/perp-2.07.tar.gz && \  
cd /root/perp-2.07 && make && make strip && make install && /usr/sbin/perp-
setup /etc/perp && \  
apk del gcc make libc-dev  
  
WORKDIR /etc/perp  
CMD /usr/sbin/perpboot  

