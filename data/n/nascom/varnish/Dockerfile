# Basic Varnish 4.1 container  
FROM debian:jessie  
  
MAINTAINER Wim Vandersmissen <wim.vandersmissen@nascom.be>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl \  
apt-transport-https \  
ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - \  
&& echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.1" >>
/etc/apt/sources.list.d/varnish-cache.list \  
&& DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
varnish \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Set timezone  
RUN ln -fs /usr/share/zoneinfo/Europe/Brussels /etc/localtime && dpkg-
reconfigure -f noninteractive tzdata  
  
ENV VARNISH_PORT 80  
ENV VARNISH_MEMORY 512m  
  
COPY run.sh /run.sh  
  
CMD ["/bin/bash", "/run.sh"]  

