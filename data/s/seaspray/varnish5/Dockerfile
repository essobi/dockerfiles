FROM ubuntu  
  
RUN apt-get update && apt-get install -y git build-essential automake
autotools-dev libedit-dev libjemalloc-dev libncurses-dev libpcre3-dev libtool
pkg-config python-docutils python-sphinx graphviz  
  
RUN git clone -b 5.0 https://github.com/varnishcache/varnish-cache.git && \  
cd varnish-cache && ./autogen.sh && \  
./configure && make && make install  
  
RUN git clone https://github.com/nigoroll/libvmod-dynamic.git && \  
cd libvmod-dynamic && ./autogen.sh && \  
./configure && make && make install && \  
ldconfig  
  
RUN mkdir /etc/varnish  
COPY default.vcl /etc/varnish  
COPY secret /etc/varnish  
  
EXPOSE 80  
ENTRYPOINT ["/usr/local/sbin/varnishd","-F"]  
CMD ["-f", "/etc/varnish/default.vcl"]  

