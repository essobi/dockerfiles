FROM debian:wheezy  
MAINTAINER Helder Correia <me@heldercorreia.com>  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV SYSMOND_VERSION 1.5.1.93  
RUN curl -s https://download.newrelic.com/server_monitor/release/newrelic-
sysmond-$SYSMOND_VERSION-linux.tar.gz \  
| tar --transform "s/^newrelic-sysmond-$SYSMOND_VERSION-linux/newrelic-
sysmond/" -xvz -C /opt  
  
WORKDIR /opt/newrelic-sysmond  
  
RUN cp nrsysmond.cfg /etc/ \  
&& cp daemon/nrsysmond.x64 /usr/bin/nrsysmond \  
&& cp scripts/nrsysmond-config /usr/bin/  
  
COPY init.sh /init  
ENTRYPOINT ["/init"]  
CMD ["nrsysmond", "-c", "/etc/nrsysmond.cfg", "-f"]  

