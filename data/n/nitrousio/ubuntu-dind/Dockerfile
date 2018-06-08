# Auto generated Dockerfile, please dont edit  
FROM ubuntu:utopic  
MAINTAINER Nitrous.IO <hello@nitrous.io>  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \  
apt-get install -yq apt-transport-https && \  
apt-get clean  
  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 && \  
echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get install -yq lxc-docker-1.4.1  
  
COPY ./dind /dind  
  
VOLUME /var/lib/docker  
ENTRYPOINT ["/dind"]  

