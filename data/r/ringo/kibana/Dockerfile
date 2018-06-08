FROM ubuntu:14.04  
ENV KIBANA_VERSION 4.0.2-linux-x64  
ENV INSTALL_DIR /usr/local/share/kibana  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y curl && \  
mkdir ${INSTALL_DIR} && \  
curl -s
https://download.elasticsearch.org/kibana/kibana/kibana-${KIBANA_VERSION}.tar.gz
| tar xz -C ${INSTALL_DIR} \--strip=1 && \  
apt-get remove -y curl && apt-get autoremove -y && apt-get clean all  
  
ADD config/kibana.yml ${INSTALL_DIR}/config/  
  
VOLUME ${INSTALL_DIR}/config  
  
EXPOSE 5601  
ENTRYPOINT ${INSTALL_DIR}/bin/kibana  

