FROM debian:stable-backports  
MAINTAINER Voob of Doom <voobscout@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive \  
GIT_SSL_NO_VERIFY 1 \  
container docker  
  
RUN apt-get update && \  
apt-get -y -q dist-upgrade && \  
apt-get install -y -q curl && \  
rm /var/log/apt/* /var/log/alternatives.log /var/log/bootstrap.log
/var/log/dpkg.log  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["weave", "10.10.0.0/16"]  

