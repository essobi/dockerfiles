FROM mesosphere/mesos-slave:1.3.1  
MAINTAINER Mesosphere <support@mesosphere.io>  
  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables \  
ipcalc \  
&& \  
apt-get clean  
  
#1.3.1 as already version 17.05.0  
# Install specific Docker version  
#ENV DOCKER_VERSION 17.05.0~ce-0~ubuntu-trusty  
#RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
# mkdir -p /etc/apt/sources.list.d && \  
# echo deb https://apt.dockerproject.org/repo ubuntu-trusty main >
/etc/apt/sources.list.d/docker.list && \  
# apt-get update -qq && \  
# DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -qqy
\  
# docker-engine=${DOCKER_VERSION} \  
# && \  
# apt-get clean  
ENV WRAPPER_VERSION 0.3.0  
COPY ./wrapdocker /usr/local/bin/  
  
ENTRYPOINT ["wrapdocker"]  
CMD ["mesos-slave"]  

