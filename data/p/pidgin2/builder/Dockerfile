FROM debian:stretch  
  
RUN set -ex && \  
echo deb-src http://httpredir.debian.org/debian stretch main | tee -a
/etc/apt/sources.list && \  
apt-get update && \  
apt-get build-dep -y pidgin && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN set -ex && \  
apt-get update && \  
apt-get install -y \  
mercurial automake autoconf libtool gtk-doc-tools curl ca-certificates && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY run.sh /  
  
CMD ["/run.sh"]  

