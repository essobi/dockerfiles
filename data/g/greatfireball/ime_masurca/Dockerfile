FROM ubuntu:xenial  
  
LABEL maintainer="frank.foerster@ime.fraunhofer.de"  
LABEL description="Dockerfile providing the MaSuRCA hybrid assembler"  
  
WORKDIR /opt/  
  
RUN apt update && apt install --yes --no-install-recommends \  
build-essential \  
libboost-dev \  
curl \  
file \  
libstatistics-descriptive-perl \  
zlib1g-dev \  
libbz2-dev && \  
curl ftp://ftp.genome.umd.edu/pub/MaSuRCA/latest/MaSuRCA-3.2.4.tar.gz >
MaSuRCA-3.2.4.tar.gz && \  
tar xzf MaSuRCA-3.2.4.tar.gz && \  
rm MaSuRCA-3.2.4.tar.gz && \  
cd MaSuRCA-3.2.4 && \  
./install.sh && \  
apt remove --yes \  
curl && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /data  
  
WORKDIR /data  
  
ENV MASURCAPATH=/opt/MaSuRCA-3.2.4  
ENV PATH=$MASURCAPATH/bin:$PATH  
ENV SR_CONFIG_EXAMPLE=$MASURCAPATH/sr_config_example.txt  
  
CMD masurca  

