FROM ubuntu:14.04  
ENV DOCKER_VERSION 1.3.3  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -qq --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
lxc \  
iptables \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -x \  
&& echo "deb https://get.docker.io/ubuntu docker main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 \  
&& apt-get update -qq \  
&& apt-get install -qq lxc-docker-$DOCKER_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
VOLUME /var/lib/docker  
CMD ["wrapdocker"]  

