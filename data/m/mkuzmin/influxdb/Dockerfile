FROM debian  
RUN VERSION=0.9.5.1 \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get -qq update \  
&& apt-get -y install wget \  
&& cd `mktemp -d` \  
&& wget -nv -O-
https://influxdb.s3.amazonaws.com/influxdb_${VERSION}_x86_64.tar.gz |tar xz
--strip 2 \  
&& mv usr/bin/* /usr/local/bin/ \  
&& rm -rf `pwd` \  
&& apt-get -y purge --auto-remove wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
COPY influxdb.conf /etc/  
VOLUME /data  
CMD ["influxd", "-config", "/etc/influxdb.conf"]  
EXPOSE 8083 8086  

