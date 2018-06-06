FROM node:slim  
MAINTAINER SFoxDev <admin@sfoxdev.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
SERVER_PORT=3000 \  
PAYLOAD_MAX_SIZE=1048576 \  
LC_ALL=C.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
RUN awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }'
/etc/apt/sources.list > /etc/apt/sources.list.d/backports.list \  
&& apt-get update \  
&& apt-get -t jessie-backports install -y git unoconv mc \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& git clone https://github.com/zrrrzzt/tfk-api-unoconv.git
/opt/unoconvservice \  
&& cd /opt/unoconvservice \  
&& npm install --production  
  
ADD update/ /opt/unoconvservice  
  
WORKDIR /opt/unoconvservice  
  
VOLUME ["/opt/unoconvservice/status"]  
  
EXPOSE 3000  
ENTRYPOINT /usr/bin/unoconv --listener --server=0.0.0.0 --port=2002 & node
standalone.js  

