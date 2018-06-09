FROM debian:jessie  
MAINTAINER Bob Maerten <hello@bobmaerten.eu>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y apt-cacher-ng && apt-get clean && rm
-rf /var/lib/apt/lists/*  
  
# redirect logs on std{out/err}  
RUN ln -sf /dev/stdout /var/log/apt-cacher-ng/apt-cacher.log \  
&& ln -sf /dev/stderr /var/log/apt-cacher-ng/apt-cacher.err  
  
# configure backends  
VOLUME ["/var/cache/apt-cacher-ng"]  
EXPOSE 3142  
CMD ["apt-cacher-ng", "-c", "/etc/apt-cacher-ng", "ForeGround=1"]  

