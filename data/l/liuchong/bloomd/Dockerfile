FROM debian:latest  
  
MAINTAINER Liu Chong <mail@clojure.cn>  
  
ENV BLOOMD_VERSION 0.7.5  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install --no-install-recommends -y \  
build-essential scons && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD https://github.com/armon/bloomd/archive/v${BLOOMD_VERSION}.tar.gz \  
/tmp/bloomd-${BLOOMD_VERSION}.tar.gz  
  
RUN mkdir /tmp/bloomd && \  
tar -xzvf /tmp/bloomd-${BLOOMD_VERSION}.tar.gz \  
-C /tmp/bloomd/ --strip-components=1 && \  
cd /tmp/bloomd/ && \  
scons && \  
mv bloomd /usr/local/bin/ && \  
rm -rf /tmp/bloomd/  
  
CMD ["bloomd"]  
  
EXPOSE 8673  

