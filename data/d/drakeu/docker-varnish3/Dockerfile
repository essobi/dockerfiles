FROM ubuntu  
MAINTAINER Dariusz Stosor <dstosor@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN curl -s http://repo.varnish-cache.org/debian/GPG-key.txt | apt-key add -  
RUN echo "deb http://repo.varnish-cache.org/ubuntu/ $(lsb_release -sc)
varnish-3.0" | tee -a /etc/apt/sources.list  
RUN echo "deb-src http://repo.varnish-cache.org/ubuntu/ $(lsb_release -sc)
varnish-3.0" | tee -a /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y --force-yes varnish=3.0.5-2  
  
ADD run.sh /run.sh  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
EXPOSE 80  
CMD /run.sh  

