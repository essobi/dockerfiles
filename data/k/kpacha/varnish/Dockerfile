FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y varnish --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /etc/varnish  
  
EXPOSE 80  
ENV VARNISH_BACKEND_ADDRESS 192.168.1.65  
ENV VARNISH_MEMORY 100M  
ENV VARNISH_BACKEND_PORT 80  
ENV VARNISH_VCL_FILE /etc/varnish/default.vcl  
ENV VARNISH_PROBE_INTERVAL 30s  
ENV VARNISH_PROBE_TIMEOUT 5s  
ENV VARNISH_GRACE_TIME 2m  
  
ADD default.vcl.source /etc/varnish/default.vcl.source  
ADD start.sh /start.sh  
  
CMD ["./start.sh"]  

