FROM ubuntu  
LABEL maintainer="Ramazan AYYILDIZ <rayyildiz@gmail.com>"  
  
ENV GRAAL_VERSION=1.0.0-rc1  
ENV
GRAAL_CE_URL=https://github.com/oracle/graal/releases/download/vm-${GRAAL_VERSION}/graalvm-
ce-${GRAAL_VERSION}-linux-amd64.tar.gz  
  
RUN apt-get update && \  
apt-get install wget -y && \  
apt-get install tar -y && \  
apt-get install gzip -y  
  
RUN cd /tmp && \  
wget $GRAAL_CE_URL -O graalvm-ce-linux-amd64.tar.gz && \  
tar -xvzf graalvm-ce-linux-amd64.tar.gz && \  
mkdir -p /usr/lib/jvm/graalvm && \  
mv graalvm-${GRAAL_VERSION} /usr/lib/jvm/graalvm && \  
rm graalvm-ce-linux-amd64.tar.gz && \  
rm -rf /usr/lib/jvm/graalvm/doc && \  
rm -rf /usr/lib/jvm/graalvm/man && \  
rm -rf /usr/lib/jvm/graalvm/src.zip && \  
rm -rf /tmp/*  
  
RUN apt-get clean  
  
ENV JAVA_HOME=/usr/lib/jvm/graalvm/graalvm-${GRAAL_VERSION}  
ENV PATH=$PATH:$JAVA_HOME/bin  
ENV GRAALVM_HOME=/usr/lib/jvm/graalvm/graalvm-${GRAAL_VERSION}  

