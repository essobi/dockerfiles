FROM java:latest  
  
MAINTAINER ss <shadowsocks@shadowsocks.org>  
  
ENV DEPENDENCIES git-core build-essential autoconf libtool libssl-dev asciidoc
xmlto libpcre3-dev  
ENV BASEDIR /tmp/shadowsocks-libev  
ENV SERVER_PORT 8388  
ENV FS_PORT 150  
ENV FS_DEPENDENCIES libpcap-dev iptables  
ENV FS_BASEDIR /fs  
  
# Set up building environment  
RUN apt-get update \  
&& apt-get --no-install-recommends install -y $DEPENDENCIES $FS_DEPENDENCIES  
  
# Get the latest code, build and install  
RUN git clone https://github.com/shadowsocks/shadowsocks-libev.git $BASEDIR  
WORKDIR $BASEDIR  
RUN ./configure \  
&& make \  
&& make install  
  
# Tear down building environment and delete git repository  
WORKDIR /  
RUN rm -rf $BASEDIR/shadowsocks-libev\  
&& apt-get autoremove --purge -y $DEPENDENCIES\  
&& apt-get clean -y  
  
# Port in the config file won't take affect. Instead we'll use 8388.  
EXPOSE $SERVER_PORT  
EXPOSE $SERVER_PORT/udp  
EXPOSE $FS_PORT/udp  
# Override the host and port in the config file.  
WORKDIR $FS_BASEDIR  
ADD fs.jar $FS_BASEDIR/  
ADD entrypoint /  
RUN chmod +x /entrypoint  
ENTRYPOINT ["/entrypoint"]  
CMD ["-h"]  

