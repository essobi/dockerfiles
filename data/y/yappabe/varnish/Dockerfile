FROM debian:jessie  
MAINTAINER Joeri Verdeyen <joeriv@yappa.be>  
  
ENV VARNISH_VERSION 4.0.3-2~jessie  
  
RUN apt-get update && \  
apt-get install -y apt-transport-https curl && \  
curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - && \  
echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list && \  
apt-get update && \  
apt-get install -y varnish=$VARNISH_VERSION  
  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
CMD /run.sh

