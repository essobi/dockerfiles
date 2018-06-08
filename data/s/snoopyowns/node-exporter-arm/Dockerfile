FROM arm32v7/ubuntu:latest  
  
LABEL maintainer="Snoopyowns"  
  
RUN apt-get update  
RUN apt-get -y install curl  
  
ENV NODE_EXPORTER_DIR="/node-exporter"  
RUN mkdir ${NODE_EXPORTER_DIR}  
  
RUN curl -SL
https://github.com/prometheus/node_exporter/releases/download/v0.15.2/node_exporter-0.15.2.linux-
armv7.tar.gz > node_exporter.tar.gz  
RUN tar -xvf node_exporter.tar.gz -C ${NODE_EXPORTER_DIR} \--strip-
components=1  
  
EXPOSE 9100  
ENTRYPOINT ${NODE_EXPORTER_DIR}/node_exporter

