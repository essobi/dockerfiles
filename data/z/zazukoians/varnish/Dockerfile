FROM phusion/baseimage  
MAINTAINER Adrian Gschwend <adrian.gschwend@zazuko.com>  
  
COPY varnishcache_varnish41.list /etc/apt/sources.list.d/  
RUN apt-get update  
RUN apt-get install -y curl gnupg apt-transport-https  
RUN curl -L https://packagecloud.io/varnishcache/varnish41/gpgkey | apt-key
add -  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
RUN apt-get -y install varnish  
  
RUN mkdir /etc/service/varnishd  
ADD run.sh /etc/service/varnishd/run  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 256m  
ENV VARNISHD_PARAMS ""  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
EXPOSE 80  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

