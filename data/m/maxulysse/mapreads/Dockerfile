FROM debian:8.6  
  
LABEL author="Maxime Garcia" \  
description="BWA 0.7.8 and SAMTools 1.3 image for use in CAW" \  
maintainer="maxime.garcia@scilifelab.se"  
#Install libraries  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
git \  
libncursesw5-dev \  
libncurses5-dev \  
make \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
#Setup ENV variables  
ENV BWA_VERSION="0.7.8" \  
SAMTOOLS_BIN="samtools-1.3.tar.bz2" \  
SAMTOOLS_VERSION="1.3"  
#Install BWA and SAMTools  
RUN git clone http://github.com/lh3/bwa.git bwa \  
&& cd bwa \  
&& git checkout $BWA_VERSION -b Docker-BWA-$BWA_VERSION \  
&& make \  
&& cp bwa /usr/local/bin/bwa \  
&& cd .. \  
&& rm -rf bwa \  
&& curl -fsSL
https://github.com/samtools/samtools/releases/download/$SAMTOOLS_VERSION/$SAMTOOLS_BIN
-o /opt/$SAMTOOLS_BIN \  
&& tar xvjf /opt/$SAMTOOLS_BIN -C /opt/ \  
&& cd /opt/samtools-$SAMTOOLS_VERSION \  
&& make \  
&& make install \  
&& rm /opt/$SAMTOOLS_BIN  

