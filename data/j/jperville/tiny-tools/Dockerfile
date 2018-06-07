FROM debian:jessie  
  
RUN echo deb http://ftp.debian.org/debian jessie-backports main | tee -a
/etc/apt/sources.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --quiet --yes --no-install-
recommends curl dnsutils netcat-openbsd jq coreutils && \  
DEBIAN_FRONTEND=noninteractive apt-get install --quiet --yes --no-install-
recommends -t jessie-backports fish && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

