FROM debian:stable-slim  
ARG RACKET_VERSION=6.12  
  
RUN apt-get update && \  
apt-get install --yes curl && \  
curl --location https://mirror.racket-
lang.org/installers/$RACKET_VERSION/racket-$RACKET_VERSION-x86_64-linux.sh >
/tmp/racket-install.sh && \  
apt-get purge --yes curl && \  
rm -rf /var/lib/apt/lists/* && \  
chmod +x /tmp/racket-install.sh && \  
echo "yes\n2\n" | /tmp/racket-install.sh && \  
rm /tmp/racket-install.sh && \  
rm -rf /usr/local/share/racket/doc  

