FROM debian:jessie  
MAINTAINER Kasumi Hanazuki <kasumi@rollingapple.net>  
  
ENV CMOGSTORED_VERSION 1.6.0  
ENV CMOGSTORED_SHA256SUM
f50d3449f3cdf8e6b67a77e42c6fc2055a7708090a52a7bebd601e3827e8a22f  
  
ADD ./setup.sh /tmp/setup.sh  
RUN /tmp/setup.sh && rm /tmp/setup.sh  
  
EXPOSE 7500 7501  
VOLUME /var/mogdata  
  
ENTRYPOINT ["/usr/local/bin/cmogstored"]  

