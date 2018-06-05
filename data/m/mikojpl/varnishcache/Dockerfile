FROM debian:stretch  
  
LABEL maintainer "mikoj@mynwt.eu"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update && \  
apt-get -y install apt-transport-https curl vim && \  
curl
https://packagecloud.io/install/repositories/varnishcache/varnish5/script.deb.sh
| bash && \  
apt-get -y install varnish && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /  
  
ADD start_varnishd.sh /start.sh  
  
ENV VARNISH_MALLOC '256m'  
ENV VARNISH_LOG 1  
ENV VARNISH_LOG_FORMAT '%h %l %u %t "%r" %s %b "%{Referer}i" "%{User-agent}i"
%{Varnish:hitmiss}x'  
RUN ln -sf /dev/stdout /var/log/varnish/access.log  
  
EXPOSE 80 6082  
RUN chmod +x /start.sh  
# Start the varnishd  
ENTRYPOINT ["./start.sh"]  

