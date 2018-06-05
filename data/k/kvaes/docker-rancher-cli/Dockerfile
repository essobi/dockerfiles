FROM ubuntu:xenial  
  
MAINTAINER Karim Vaes <dockerfile@kvaes.be>  
  
# Rancher CLI Source : https://github.com/rancher/cli/releases/  
ARG RANCHER_VERSION=v0.2.0-rc1  
ARG RANCHER_PACKAGE=rancher-linux-amd64-v0.2.0-rc1.tar.gz  
ARG RANCHER_CLIHOME=/usr/lib/rancher-cli  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https ca-certificates curl \  
&& echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& apt-get update -y \  
&& apt-get install -y docker-engine \  
&& mkdir ${RANCHER_CLIHOME} \  
&& curl -SLO
"https://github.com/rancher/cli/releases/download/${RANCHER_VERSION}/${RANCHER_PACKAGE}"
\  
&& tar -xzf ${RANCHER_PACKAGE} -C /tmp \  
&& mv /tmp/rancher-${RANCHER_VERSION}/rancher ${RANCHER_CLIHOME} \  
&& rm -rf /tmp/rancher* \  
&& rm ${RANCHER_PACKAGE}  
  
VOLUME ${RANCHER_CLIHOME}  
  
ENTRYPOINT ["/usr/lib/rancher-cli/rancher"]  
CMD ["--help"]

