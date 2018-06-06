FROM ubuntu:latest  
MAINTAINER nagev <np1nagev@gmail.com>  
  
# https://github.com/np1/docker-tor-clientonly  
# Based on https://github.com/patrickod/docker-tor  
  
ENV TORNAME tor-0.2.8.7  
  
RUN set -ex \  
&& buildDeps='libwww-perl build-essential libevent-dev libssl-dev wget' \  
&& apt-get update \  
&& apt-get install -y $buildDeps \  
&& wget -qO - https://www.torproject.org/dist/${TORNAME}.tar.gz | tar xvz -C
/tmp \  
&& ( cd /tmp/${TORNAME} \  
&& ./configure \  
&& make \  
&& make install ) \  
&& rm -rf /tmp/${TORNAME} \  
&& echo "Log notice stdout" >> /etc/torrc \  
&& echo "SocksPort 0.0.0.0:9150" >> /etc/torrc \  
&& apt-get purge -y $buildDeps \  
&& apt-get clean  
  
EXPOSE 9150  
  
CMD /usr/local/bin/tor -f /etc/torrc  

