FROM maxulysse/gatk:1.1  
LABEL author="Maxime Garcia" \  
description="GATK 3.7, Picard 2.0.1, R 3.3.2 and VarDictJava 1.4.5 image for
use in CAW" \  
maintainer="maxime.garcia@scilifelab.se"  
  
# Install libraries  
RUN apt-get update && apt-get install -y --no-install-recommends \  
r-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# Setup ENV variables  
ENV PATH="$PATH:/opt/VarDictJava:/opt/VarDictJava/VarDict" \  
PICARD_BIN="picard-tools-2.0.1.zip" \  
PICARD_HOME="/opt/picard-tools-2.0.1" \  
PICARD_VERSION="2.0.1" \  
VARDICTJAVA_BIN="v1.4.5.zip" \  
VARDICTJAVA_VERSION="1.4.5"  
# Install Picard, VarDict and VarDictJava  
RUN curl -fsSL
https://github.com/broadinstitute/picard/releases/download/$PICARD_VERSION/$PICARD_BIN
-o /opt/$PICARD_BIN \  
&& unzip /opt/$PICARD_BIN -d /opt/ \  
&& rm /opt/$PICARD_BIN \  
&& curl -fsSL https://github.com/AstraZeneca-
NGS/VarDictJava/archive/$VARDICTJAVA_BIN -o /opt/$VARDICTJAVA_BIN \  
&& unzip /opt/$VARDICTJAVA_BIN -d /opt/ \  
&& mv /opt/VarDictJava-$VARDICTJAVA_VERSION /opt/VarDictJava \  
&& rm /opt/$VARDICTJAVA_BIN \  
&& git clone git://github.com/AstraZeneca-NGS/VarDict.git
/opt/VarDictJava/VarDict  

