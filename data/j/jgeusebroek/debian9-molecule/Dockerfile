FROM debian:stretch  
MAINTAINER Jeroen Geusebroek <me@jeroengeusebroek.nl>  
  
COPY files/initctl_faker .  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
systemd \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean \  
  
&& chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker
/sbin/initctl  

