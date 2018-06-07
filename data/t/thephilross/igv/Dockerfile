# IGV docker container  
FROM ubuntu:14.04  
MAINTAINER Philipp Ross, philippross369@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
software-properties-common \  
default-jre \  
wget \  
unzip \  
glib-networking-common  
  
RUN mkdir -p /igv && \  
cd /igv && \  
wget http://www.broadinstitute.org/igv/projects/downloads/IGV_2.3.42.zip && \  
unzip IGV_2.3.42.zip && \  
cd IGV_2.3.42/ && \  
sed -i 's/Xmx2000/Xmx8000/g' igv.sh && \  
cd /usr/bin && \  
ln -s /igv/IGV_2.3.42/igv.sh ./igv  
  
CMD ["/usr/bin/igv"]

