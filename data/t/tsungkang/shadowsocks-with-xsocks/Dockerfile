FROM java:latest  
  
MAINTAINER ss <shadowsocks@shadowsocks.org>  
  
ENV DEPENDENCIES git-core build-essential autoconf libtool libssl-dev asciidoc
xmlto libpcre3-dev  
ENV BASEDIR /tmp/shadowsocks-libev  
ENV SERVER_PORT 8338  
ENV XS_PORT 130  
ENV XS_DEPENDENCIES libpcap-dev iptables  
ENV XS_BASEDIR /xs  
  
# Set up building environment  
RUN apt-get update \  
&& apt-get --no-install-recommends install -y $DEPENDENCIES $XS_DEPENDENCIES  
  
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
  
# Get TcpSpeed  
RUN if [ ! -d "$XS_BASEDIR" ]; then mkdir $XS_BASEDIR; fi  
WORKDIR $XS_BASEDIR  
RUN wget -O xsocks_server.zip
http://www.tcpspeed.com/tcpspeed/tcpspeed_server.zip &&\  
unzip xsocks_server.zip && rm -f xsocks_server.zip && if [ ! -d
"$XS_BASEDIR/cnf" ]; then mkdir $XS_BASEDIR/cnf; fi  
  
# Port in the config file won't take affect. Instead we'll use 8388.  
EXPOSE $SERVER_PORT  
EXPOSE $SERVER_PORT/udp  
EXPOSE $XS_PORT/udp  
  
# Override the host and port in the config file.  
ADD entrypoint /  
RUN chmod +x /entrypoint  
ENTRYPOINT ["/entrypoint"]  
CMD ["-h"]  

