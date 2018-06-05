FROM ubuntu:14.04  
MAINTAINER ATSD Developers <dev-atsd@axibase.com>  
ENV s=60  
ENV c=1440  
RUN apt-get update && \  
apt-get install -y curl lshw || yum install -y curl lshw net-tools  
WORKDIR /opt/nmon  
  
RUN curl -L -o nmon
https://github.com/axibase/nmon/releases/download/16d/nmon_x86_ubuntu && \  
chmod +x nmon  
RUN curl -o entrypoint.sh
https://raw.githubusercontent.com/axibase/dockers/nmon/entrypoint.sh && \  
chmod +x entrypoint.sh  
  
ENTRYPOINT ["/opt/nmon/entrypoint.sh"]  
  

