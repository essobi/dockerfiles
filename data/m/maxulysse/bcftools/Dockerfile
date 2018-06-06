FROM debian:8.6  
LABEL author="Maxime Garcia" \  
description="BCFTools 1.3 image for use in CAW" \  
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
ENV BCFTOOLS_BIN="bcftools-1.3.tar.bz2" \  
BCFTOOLS_PLUGINS="/usr/local/libexec/bcftools" \  
BCFTOOLS_VERSION="1.3"  
#Install BCFTools  
RUN curl -fsSL
https://github.com/samtools/bcftools/releases/download/$BCFTOOLS_VERSION/$BCFTOOLS_BIN
-o /opt/$BCFTOOLS_BIN \  
&& tar xvjf /opt/$BCFTOOLS_BIN -C /opt/ \  
&& cd /opt/bcftools-$BCFTOOLS_VERSION \  
&& make \  
&& make install \  
&& rm -rf /opt/$BCFTOOLS_BIN /opt/bcftools-$BCFTOOLS_VERSION  

