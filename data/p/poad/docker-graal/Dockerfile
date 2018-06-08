FROM ubuntu:latest  
  
LABEL Kenji Saito "ken-yo@mbr.nifty.com"  
  
ENV GRAAL_VM_VERSION 1.0.0-rc2  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y -qq \  
curl \  
bash \  
ca-certificates && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL
https://github.com/oracle/graal/releases/download/vm-${GRAAL_VM_VERSION}/graalvm-
ce-${GRAAL_VM_VERSION}-linux-amd64.tar.gz | tar -xz -C /usr/local && \  
ln -s /usr/local/graalvm-${GRAAL_VM_VERSION} /usr/local/graalvm  
  
ENV JAVA_HOME /usr/local/graalvm  
ENV PATH ${JAVA_HOME}/bin:${PATH}  

