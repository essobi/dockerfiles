FROM debian:stretch  
  
RUN apt-get update && apt-get install -y apt-cacher-ng --no-install-recommends
\  
&& sed 's/# ForeGround: 0/ForeGround: 1/' -i /etc/apt-cacher-ng/acng.conf \  
&& sed 's/# PassThroughPattern:.*this would allow.*/PassThroughPattern: .* #/'
-i /etc/apt-cacher-ng/acng.conf \  
&& rm -rf /var/lib/apt/lists/*  
  
# For pre-1.13 Dockers (*cough* SYNOLOGY *cough*)  
ADD https://github.com/krallin/tini/releases/download/v0.14.0/tini /tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
EXPOSE 3142/tcp  
VOLUME ["/var/cache/apt-cacher-ng"]  
CMD ["/usr/sbin/apt-cacher-ng", "-c", "/etc/apt-cacher-ng"]  

