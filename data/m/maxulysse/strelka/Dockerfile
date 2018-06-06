FROM debian:8.6  
LABEL author="Maxime Garcia" \  
description="Strelka 1.0.15 image for use in CAW" \  
maintainer="maxime.garcia@scilifelab.se"  
  
#Install libraries  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
ca-certificates \  
curl \  
g++ \  
make \  
perl-doc \  
python \  
rsync \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
#Setup ENV variables  
ENV STRELKA_BIN="strelka_workflow-1.0.15.tar.gz" \  
STRELKA_INSTALL_DIR="/opt/strelka/" \  
STRELKA_VERSION="1.0.15"  
#Install Strelka  
RUN curl -fsSL
https://sites.google.com/site/strelkasomaticvariantcaller/home/download/$STRELKA_BIN
-o $STRELKA_BIN \  
&& tar xf $STRELKA_BIN \  
&& rm -f $STRELKA_BIN \  
&& cd strelka_workflow-$STRELKA_VERSION \  
&& ./configure --prefix=$STRELKA_INSTALL_DIR \  
&& make  

