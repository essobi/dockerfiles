#  
# This is unofficial dockerized precompiled i2pd within a debian:stable-slim
image (~ 65 Mb).  
#  
FROM debian:stable-slim  
MAINTAINER Bob <kcey@mail.ru>  
  
ENV I2PD_URL=https://api.github.com/repos/PurpleI2P/i2pd/releases  
ENV I2PD_RELEASE="latest"  
ENV DEBIAN_CODENAME="stretch"  
ENV PARAMS="--bandwidth P --share 50 --limits.transittunnels 256
--upnp.enabled true --http.address 0.0.0.0 --httpproxy.address 0.0.0.0
--socksproxy.address 0.0.0.0 --sam.enabled true --sam.address 0.0.0.0"  
COPY start_i2pd.sh /start_i2pd.sh  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& chmod a+x /start_i2pd.sh \  
&& apt-get update && apt-get upgrade -y \  
&& apt-get install --no-install-recommends -y ca-certificates wget curl \  
&& mkdir /tmp/i2pd && cd /tmp/i2pd \  
&& wget --tries=3 $(curl -s $I2PD_URL/$I2PD_RELEASE | \  
grep browser_download_url | \  
egrep -o 'http.+\\.\w+' | \  
grep -m 1 -i "$(if [ "$DEBIAN_CODENAME" != "*" ]; then echo $DEBIAN_CODENAME;
else cat /etc/*-release | grep VERSION= | egrep -o '\\(.+\\)' | tr -d "()";
fi)" | \  
grep -i "$(dpkg --print-architecture)") \  
&& apt-get install --no-install-recommends -f -y ./*.deb \  
&& apt-get purge -y -q --auto-remove ca-certificates wget curl \  
&& apt-get clean \  
&& cd / \  
&& rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/* \  
  
VOLUME [ "/var/lib/i2pd" ]  
  
EXPOSE 7070 4444 4447 7656 2827 7654 7650  
ENTRYPOINT ["/start_i2pd.sh"]  

