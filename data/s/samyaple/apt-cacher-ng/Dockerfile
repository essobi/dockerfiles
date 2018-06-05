FROM ubuntu:xenial  
#ENV DEBIAN_FRONTEND noninteractive  
RUN set -eux ; \  
apt-get update ; \  
apt-get install -y --no-install-recommends \  
curl \  
ca-certificates \  
apt-cacher-ng \  
; \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/sbin/apt-cacher-ng"]  
CMD ["-c", "/etc/apt-cacher-ng", "ForeGround=1"]  
  
# A standard build and run command look like the following lines  
#  
# root ~ # docker build -t apt-cacher-ng .  
# root ~ # docker run -d -t --restart=always -v /etc/apt-cacher-ng/:/etc/apt-
cacher-ng/ -v apt-cacher-ng:/var/cache/apt-cacher-ng/ --net host --name apt-
cacher-ng apt-cacher-ng  

