# http://bio-bwa.sourceforge.net/  
FROM debian:jessie  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
bzip2 \  
ca-certificates \  
curl \  
gcc \  
libc6-dev \  
make \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install bwa  
ENV BWA_VERSION 0.7.15  
RUN curl -SL https://sourceforge.net/projects/bio-
bwa/files/bwa-$BWA_VERSION.tar.bz2/download --output bwa.tar.bz2 \  
&& tar -xjf bwa.tar.bz2 \  
&& rm bwa.tar.bz2 \  
&& cd bwa-$BWA_VERSION \  
&& make \  
&& cd .. \  
&& ln -s /bwa-$BWA_VERSION/bwa /usr/bin/bwa  
  
ENTRYPOINT ["bwa"]  

