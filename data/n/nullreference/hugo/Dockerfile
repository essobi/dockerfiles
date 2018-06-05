FROM debian:jessie-slim  
LABEL maintainer="lucas-natraj"  
  
ENV HUGO_VER 0.32.3  
RUN apt-get update && \  
apt-get install unzip wget -y && \  
wget -q -P /tmp -O hugo.tar.gz
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VER}/hugo_${HUGO_VER}_Linux-64bit.tar.gz
&& \  
mkdir -p /opt/hugo && \  
tar -zxf hugo.tar.gz --directory /opt/hugo && \  
echo '#!/bin/bash\n/opt/hugo/hugo $@' > /usr/bin/hugo && \  
chmod +x /usr/bin/hugo && \  
rm -f /tmp/*  
  
ENTRYPOINT [ "hugo" ]  
# CMD ["help"]  

