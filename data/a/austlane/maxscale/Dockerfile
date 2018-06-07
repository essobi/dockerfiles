FROM debian:jessie  
MAINTAINER Austin Lane <austin@sellerlabs.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MAXSCALE_VERSION 2.0.1  
RUN echo "deb http://downloads.mariadb.com/enterprise/6whk-mygr/mariadb-
maxscale/${MAXSCALE_VERSION}/debian jessie main" | tee -a
/etc/apt/sources.list.d/maxscale.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8167EE24 &&
\  
apt-get update -qq && \  
apt-get install -y maxscale && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
CMD ["/usr/bin/maxscale", "-d"]

