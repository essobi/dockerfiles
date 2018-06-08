FROM debian:jessie  
  
ENV DEBIAN_FRONTEND=noninteractive \  
CHRONOGRAF_VERSION=0.3.2 \  
CHRONOGRAF_BIND=0.0.0.0:3000  
RUN apt-get update && \  
apt-get install -y wget && \  
wget
https://s3.amazonaws.com/get.influxdb.org/chronograf/chronograf_${CHRONOGRAF_VERSION}_amd64.deb
&& \  
dpkg -i chronograf_${CHRONOGRAF_VERSION}_amd64.deb && \  
rm chronograf_${CHRONOGRAF_VERSION}_amd64.deb  
  
EXPOSE 3000  
CMD ["/opt/chronograf/chronograf", "-config=/opt/chronograf/config.toml"]  

