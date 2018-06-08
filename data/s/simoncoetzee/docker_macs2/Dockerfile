FROM ubuntu:14.04  
  
MAINTAINER Simon Coetzee "simon.coetzee@cshs.org"  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y wget bedtools samtools \  
libopenblas-base libopenblas-dev \  
liblapack3 liblapack-dev  
  
### macs2  
RUN apt-get install -y python python-pip python-dev  
RUN pip install numpy  
RUN pip install macs2  
  
COPY run.sh /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
CMD ["run"]  
VOLUME /data  

