FROM debian:jessie  
MAINTAINER Kamil Cholewiński <kamil@unit9.com>  
  
RUN apt-get update && \  
apt-get dist-upgrade --yes && \  
apt-get install --no-install-recommends --yes \  
apt-transport-https \  
bzip2 \  
ca-certificates \  
curl \  
runit \  
socklog \  
&& \  
rm -rf /var/cache/apt /var/lib/apt/lists  
  
RUN curl -fsSL -o /tmp/runsvinit.tgz \  
https://github.com/peterbourgon/runsvinit/releases/download/v2.0.0/runsvinit-
linux-amd64.tgz \  
&& sha256sum /tmp/runsvinit.tgz \  
&& cd /sbin \  
&& tar zxf /tmp/runsvinit.tgz \  
&& chown root:root /sbin/runsvinit \  
&& rm /tmp/runsvinit.tgz  
ADD rc rc.local /etc/  
ADD socklog.run /etc/service/socklog/run  
CMD ["/etc/rc"]  

