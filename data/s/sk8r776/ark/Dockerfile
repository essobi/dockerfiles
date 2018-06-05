FROM ubuntu:latest  
  
MAINTAINER Sk8r776  
  
# Starting steam with validate is slow, lets make it an option  
ENV CHECKFILES "false"  
# Variable to enable RCON, enabled by default  
ENV RCON "true"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get -y install lib32gcc1 wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean \  
&& mkdir -p /data/containerdata/ark/1/backup \  
&& useradd -d /data/containerdata/ark/1/ark -s /bin/bash --uid 1000 ark \  
&& chown -R ark: /data/containerdata/ark/1  
  
EXPOSE 27015/udp 7778/udp  
EXPOSE 32330/tcp  
  
RUN mkdir -p /tmp/ark \  
&& wget https://raw.githubusercontent.com/sk8r776/docker-ark/master/ark.sh -O
/tmp/ark/ark1.sh \  
&& mv /tmp/ark/ark1.sh /usr/local/bin/ark \  
&& chmod +x /usr/local/bin/ark  
  
USER ark  
VOLUME /data/containerdata/ark/1  
WORKDIR /data/containerdata/ark/1  
CMD ["ark"]

