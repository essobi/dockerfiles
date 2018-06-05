FROM ubuntu:latest  
MAINTAINER Philipp Schmitt <philipp@schmitt.co>  
  
ENV ARCH=x86_64  
  
RUN apt-get -y update && apt-get install -y git && \  
git clone https://github.com/50ButtonsEach/fliclib-linux-hci /tmp/src && \  
cp /tmp/src/bin/${ARCH}/flicd /usr/bin/flicd && \  
chmod +x /usr/bin/flicd && \  
mkdir /config && \  
rm -rf /tmp/src && \  
apt-get remove --purge -y git && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /config  
VOLUME ["/config"]  
EXPOSE 5551  
ENTRYPOINT ["/usr/bin/flicd", "-f", "/config/db", "-s", "0.0.0.0", "-p",
"5551"]  

