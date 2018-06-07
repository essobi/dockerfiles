FROM debian:jessie  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
unzip \  
gdal-bin \  
postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget --quiet -P /tmp
https://swissnames.os.zhdk.cloud.switch.ch/swissNAMES3D.zip \  
&& unzip -d /swisstopo /tmp/swissNAMES3D.zip \  
&& rm -rf /tmp  
  
ENV TOPO_DATA_DIR="/swisstopo"  
WORKDIR /usr/src/app  
COPY ./ /usr/src/app  
CMD ["./import-swisstopo.sh"]  

