FROM debian:jessie  
MAINTAINER John Gedeon <js1@gedeons.com>  
  
# let debian know we are not interactive  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install some packages  
RUN apt-get update &&\  
apt-get -y upgrade &&\  
apt-get -y install ca-certificates nginx-light ruby ruby-dev \  
build-essential ruby-execjs \  
git golang wget &&\  
gem install bundler daemons faraday  
  
# setup root  
USER root  
ENV HOME=/root  
WORKDIR /root  
  
# Install confd incase we need it  
RUN wget
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64  
RUN mv confd-0.10.0-linux-amd64 /usr/local/bin/confd && chmod 755
/usr/local/bin/confd  
RUN mkdir -p /etc/confd/{conf.d,templates}  
  
# add utilities  
COPY bin/* /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
COPY lib/* /root/  
  
# Clean up temp files  
RUN apt-get clean &&\  
rm -rf /tmp/* /var/tmp/* &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /etc/dpkg/dpkg.cfg.d/02apt-speedup  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
RUN ln -sf /dev/stdout /var/log/confd.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["start-up.sh"]  

