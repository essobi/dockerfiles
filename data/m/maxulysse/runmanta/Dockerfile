FROM debian:8.6  
  
LABEL author="Maxime Garcia" \  
description="Manta 1.0.3 and SAMTools 1.3 image for use in CAW" \  
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
python2.4 \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
#Setup ENV variables  
ENV MANTA_BIN="manta-1.0.3.centos5_x86_64.tar.bz2" \  
MANTA_INSTALL_PATH="/opt/manta-1.0.3" \  
MANTA_VERSION="v1.0.3" \  
SAMTOOLS_BIN="samtools-1.3.tar.bz2" \  
SAMTOOLS_VERSION="1.3"  
#Install SAMTools & Manta  
RUN curl -fsSL
https://github.com/Illumina/manta/releases/download/$MANTA_VERSION/$MANTA_BIN
-o /opt/$MANTA_BIN \  
&& tar xvjf /opt/$MANTA_BIN -C /opt/ \  
&& mv /opt/manta-1.0.3.centos5_x86_64 $MANTA_INSTALL_PATH \  
&& curl -fsSL
https://github.com/samtools/samtools/releases/download/$SAMTOOLS_VERSION/$SAMTOOLS_BIN
-o /opt/$SAMTOOLS_BIN \  
&& tar xvjf /opt/$SAMTOOLS_BIN -C /opt/ \  
&& cd /opt/samtools-$SAMTOOLS_VERSION \  
&& make \  
&& make install \  
&& rm /opt/$SAMTOOLS_BIN /opt/$MANTA_BIN  

