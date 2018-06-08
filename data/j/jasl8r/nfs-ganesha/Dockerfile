FROM ubuntu:14.04  
MAINTAINER Jeremy Slater <jasl8r@alum.wpi.edu>  
  
ENV GANESHA_VERSION=2.4.2 \  
S6_OVERLAY_VERSION=1.19.1.1 \  
DOCKERIZE_VERSION=0.3.0  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install -y python-setuptools wget \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3FE869A9 \  
&& echo "deb http://ppa.launchpad.net/gluster/nfs-ganesha/ubuntu trusty main"
| tee /etc/apt/sources.list.d/nfs-ganesha.list \  
&& echo "deb http://ppa.launchpad.net/gluster/libntirpc/ubuntu trusty main" |
tee /etc/apt/sources.list.d/libntirpc.list \  
&& apt-get update \  
&& apt-get install -y nfs-ganesha=${GANESHA_VERSION}* nfs-ganesha-
fsal=${GANESHA_VERSION}* \  
&& wget https://github.com/just-
containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz \  
&& tar xzf s6-overlay-amd64.tar.gz -C / \  
&& rm s6-overlay-amd64.tar.gz \  
&& wget
https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-
amd64-v${DOCKERIZE_VERSION}.tar.gz \  
&& rm dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \  
&& apt-get autoremove -y python-setuptools wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY rpcbind /etc/services.d/rpcbind/run  
COPY rpc.statd /etc/services.d/rpc.statd/run  
COPY ganesha.conf.tmpl /etc/ganesha/ganesha.conf.tmpl  
  
EXPOSE 111 111/udp 662 2049 38465-38467  
ENV S6_CMD_WAIT_FOR_SERVICES=0  
ENTRYPOINT ["/init"]  
CMD ["dockerize", \  
"-template", "/etc/ganesha/ganesha.conf.tmpl:/etc/ganesha/ganesha.conf", \  
"ganesha.nfsd", "-F", "-L", "/dev/stdout", "-f", "/etc/ganesha/ganesha.conf"]  

