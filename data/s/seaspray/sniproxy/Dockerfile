FROM ubuntu  
  
RUN apt-get update && apt-get install -y git autotools-dev cdbs debhelper dh-
autoreconf dpkg-dev gettext libev-dev libpcre3-dev libudns-dev pkg-config
fakeroot devscripts  
  
RUN git clone https://github.com/dlundquist/sniproxy.git && \  
cd sniproxy && ./autogen.sh && \  
./configure && make install  
  
ENTRYPOINT ["/usr/local/sbin/sniproxy","-f"]  
  
EXPOSE 80 443  
CMD ["-c", "/etc/sniproxy.conf"]  

