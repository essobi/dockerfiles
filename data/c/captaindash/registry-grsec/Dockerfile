#  
# Dockerfile for Docker Registry with grsecurity kernel  
#  
# VERSION 2.5.1-2  
FROM debian:jessie  
  
ADD bin/registry /bin/registry  
ADD conf/config-example.yml /etc/docker/registry/config.yml  
ADD entrypoint /entrypoint  
  
VOLUME ["/var/lib/registry"]  
EXPOSE 5000  
RUN echo 'deb http://debian.mirrors.ovh.net/debian jessie main' >
/etc/apt/sources.list \  
&& echo 'deb http://debian.mirrors.ovh.net/debian jessie-updates main' >>
/etc/apt/sources.list \  
&& echo 'deb http://security.debian.org jessie/updates main' >>
/etc/apt/sources.list \  
&& echo 'deb http://debian.mirrors.ovh.net/debian jessie-backports main
contrib non-free' > /etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -t jessie-backports -y --no-install-recommends \  
ca-certificates \  
openssl \  
apache2-utils \  
attr \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& chmod u+x /entrypoint \  
&& chmod u+x /bin/registry  
  
ENTRYPOINT ["/entrypoint"]  
CMD ["/etc/docker/registry/config.yml"]  

