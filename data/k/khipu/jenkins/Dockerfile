FROM jenkins:latest  
MAINTAINER developers@khipu.com  
  
ARG GOSU_VERSION=1.7  
USER root  
  
RUN echo 'America/Santiago' > /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y thrift-compiler curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& groupmod -g 2000 jenkins \  
&& usermod -u 2000 -g 2000 jenkins  
  
RUN curl -o /usr/local/bin/gosu -fsSL
https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64 \  
&& chmod +x /usr/local/bin/gosu  
  
ADD init.sh /  
  
ENTRYPOINT ["/init.sh"]

