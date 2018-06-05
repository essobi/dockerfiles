FROM debian:jessie  
MAINTAINER David McCullars <david@bloomfire.com>  
  
ADD etc/apt /etc/apt  
RUN apt-get update -y && \  
apt-get install -y \  
haproxy \  
inotify-tools \  
runit  
RUN mkdir -p /var/run/container-change /run/haproxy && \  
touch /var/run/container-change  
  
VOLUME /var/run/container-change  
  
ENV DOCKER_GEN_VERSION 0.7.3  
ADD https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
/usr/local/bin  
  
EXPOSE 80  
ADD bin /bin  
ADD etc /etc  
  
ENTRYPOINT ["/bin/start-services.sh"]  

