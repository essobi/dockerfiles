FROM debian:jessie  
  
  
RUN echo "==> install haka dependencies" \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
\  
dialog apt-utils\  
git make build-essential cppcheck valgrind\  
cmake swig check rsync gawk libpcap-dev libedit-dev libpcre3-dev tshark \  
iptables libnetfilter-queue-dev uuid-dev libcurl4-openssl-dev libssl-dev  
  
RUN echo "==> install hakabana dependencies" \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
\  
libgeoip-dev libjansson-dev libuuid1 geoip-database  
  
  
RUN echo "==> install haka" \  
&& cd /tmp \  
&& git config --global http.sslVerify false \  
&& git clone https://github.com/haka-security/haka.git \  
&& cd haka \  
&& git submodule init \  
&& git submodule update \  
&& mkdir -p make \  
&& cd make \  
&& cmake .. \  
&& make \  
&& make install  
  
RUN echo "==> install hakabana" \  
&& cd /tmp \  
&& git config --global http.sslVerify false \  
&& git clone https://github.com/haka-security/hakabana.git \  
&& cd hakabana \  
&& mkdir -p make \  
&& cd make \  
&& cmake .. \  
&& make \  
&& make install  
  
RUN echo "==> install dns server unbound" \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
wget unbound supervisor \  
&& cd /var/lib/unbound/ && wget ftp://ftp.internic.net/domain/named.cache \  
&& mv named.cache root.hints && chown unbound:unbound root.hints  
  
COPY unbound.conf /etc/unbound/unbound.conf  
COPY root.key /var/lib/unbound/root.key  
COPY supervisord.conf /etc/supervisor/conf.d/  
RUN unbound-checkconf  
  
  
RUN echo "==> install some tools" \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
\  
wget nano unzip net-tools socat rsyslog \  
&& rm -rf /var/lib/apt/lists/*  
  
  
RUN echo "==> build luajit interpreter " \  
&& cd /tmp/haka/external/luajit/src \  
&& make && make install  
  
  
RUN echo "==> install luarocks " \  
&& cd /usr/local/bin && ln -s luajit-2.0.4 lua \  
&& cd /tmp \  
&& git clone git://github.com/luarocks/luarocks.git \  
&& cd luarocks \  
&& ./configure --with-lua=/usr/local --with-lua-
include=/tmp/haka/external/luajit/src/src \  
&& make build && make install \  
&& luarocks install luasocket \  
&& luarocks install redis-lua  
#&& luarocks install posix  
  
  
#  
# custom  
#  
ADD rsyslog.conf /etc/rsyslog.conf  
  
  
ADD files/config.lua /usr/local/share/haka/hakabana/config.lua  
ADD files/ /tmp/  
RUN chmod +x /tmp/tests/*.sh /tmp/tests/*/*.sh  
  
# CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  
CMD ["/usr/bin/supervisord"]  

