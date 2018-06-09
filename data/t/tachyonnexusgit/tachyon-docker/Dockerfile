FROM maven:3.3.3-jdk-7  
MAINTAINER TachyonNexus  
  
# Get Tachyon from github release.  
ENV TACHYON_VERSION 0.7.0  
RUN mkdir -p /opt && \  
cd /opt && \  
wget
https://github.com/amplab/tachyon/releases/download/v$TACHYON_VERSION/tachyon-$TACHYON_VERSION-
bin.tar.gz && \  
tar -zvxf tachyon-$TACHYON_VERSION-bin.tar.gz && \  
rm tachyon-$TACHYON_VERSION-bin.tar.gz && \  
ln -s tachyon-$TACHYON_VERSION tachyon && \  
cd tachyon && \  
mvn install && \  
echo Tachyon installed in /opt  
  
ENV PATH $PATH:/opt/tachyon/bin  

