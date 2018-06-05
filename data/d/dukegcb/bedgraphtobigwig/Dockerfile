FROM phusion/baseimage  
MAINTAINER Alejandro Barrera <alejandro.barrera@duke.edu>  
  
# Install python (+devs) and essentials for building  
RUN apt-get update && apt-get install -y \  
curl && \  
apt-get clean autoclean && \  
apt-get autoremove -y  
  
ENV BEDGRAPHTOBIGWIG_VERSION=287  
ENV
BEDGRAPHTOBIGWIG_URL=http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64.v${BEDGRAPHTOBIGWIG_VERSION}/bedGraphToBigWig  
ENV DEST_DIR=/usr/local/bin/  
  
# Download bedGraphToBigWig file  
RUN curl -SLo ${DEST_DIR}/bedGraphToBigWig ${BEDGRAPHTOBIGWIG_URL} && \  
chmod +x ${DEST_DIR}/bedGraphToBigWig  
  
# Default command to execute at startup of the container  
CMD ["bedGraphToBigWig"]

