FROM shift/ubuntu:15.04  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
WORKDIR /tmp  
RUN apt-get update \  
&& apt-get install curl --yes \  
&& curl -O https://s3.amazonaws.com/influxdb/influxdb_0.9.3_amd64.deb \  
&& dpkg -i influxdb_0.9.3_amd64.deb \  
&& rm influxdb_0.9.3_amd64.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD files/run.sh /run.sh  
ADD files/config.toml /config/config.toml  
ENV PRE_CREATE_DB **None**  
ENV SSL_SUPPORT **False**  
ENV SSL_CERT **None**  
  
EXPOSE 2003  
EXPOSE 8083  
EXPOSE 8086  
EXPOSE 8090  
EXPOSE 8099  
VOLUME ["/data"]  
  
CMD ["/run.sh"]  

