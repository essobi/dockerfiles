FROM debian:stretch  
  
# docker build . --build-arg APT_PROXY="http://apt-proxy.local:3142" -t
katta/vacanze  
ARG APT_PROXY  
RUN [ -z "$APT_PROXY" ] || /bin/echo -e "Acquire::HTTP::Proxy
\"$APT_PROXY\";\nAcquire::HTTPS::Proxy
\"$APT_PROXY\";\nAcquire::http::Pipeline-Depth \"23\";" >
/etc/apt/apt.conf.d/01proxy  
  
RUN set -x && \  
apt-get update -qq && \  
apt-get install -y python wget aircrack-ng && \  
wget http://wpa-sec.stanev.org/hc/help_crack.py -O /help_crack.py && \  
chmod +x /help_crack.py && \  
apt-get autoremove --purge -y wget && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /workdir  
  
WORKDIR /workdir  
VOLUME /workdir  
  
CMD [ "/help_crack.py" ]

