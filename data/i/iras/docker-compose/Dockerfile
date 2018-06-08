FROM ubuntu:16.04  
MAINTAINER Thomas Flori <tflori@pb-systems.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
  
# speedup apt  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb http://apt.dockerproject.org/repo ubuntu-xenial main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update -q \  
&& apt-get upgrade -yqq  
  
RUN apt-get -yq --no-install-recommends install \  
python-pip \  
docker-engine \  
python \  
openssh-client \  
&& pip install -U setuptools \  
&& pip install docker-compose \  
&& apt-get --purge -yq autoremove python-pip \  
&& apt-get clean -q \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV DOCKER_HOST tcp://docker:2375  

