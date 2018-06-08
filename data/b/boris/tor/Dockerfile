# docker run -d --name tor_nado -p 192.168.99.100:9150:9150 boris/tor:1.0  
FROM ubuntu:latest  
MAINTAINER Boris Quiroz <boris@insert-coin.org>  
  
ENV TORNAME tor-0.2.7.6  
RUN apt-get update  
RUN apt-get install -yq --no-install-recommends libwww-perl build-essential
libevent-dev libssl-dev  
RUN GET https://www.torproject.org/dist/${TORNAME}.tar.gz | tar xz -C /tmp  
  
RUN cd /tmp/${TORNAME} && ./configure  
RUN cd /tmp/${TORNAME} && make  
RUN cd /tmp/${TORNAME} && make install  
RUN rm -rf /tmp/${TORNAME}  
  
EXPOSE 9150  
RUN echo "Log notice stdout" >> /etc/torrc  
RUN echo "SocksPort 0.0.0.0:9150" >> /etc/torrc  
  
CMD /usr/local/bin/tor -f /etc/torrc  

