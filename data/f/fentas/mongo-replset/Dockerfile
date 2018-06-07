FROM mongo:3.0  
MAINTAINER Jan Guth <jan.guth@gmail.com>  
  
ENV SERVICE "mongo"  
ENV MONGO_REPLSET "rs0"  
ENV VERBOSE 6  
ENV META_URL "http://rancher-metadata/2015-07-25"  
ENV HOST_LABEL "mongo"  
ENV INTERVAL 30  
ENV MAINTENANCE "@daily"  
ENV AUTHENTICATION ""  
ENV PORT 27017  
RUN \  
apt-get update && \  
apt-get install -y \  
dnsutils && \  
apt-get remove -y \  
perl && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true && \  
find /usr/share/doc -empty|xargs rmdir || true && \  
rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* && \  
rm -rf /usr/share/lintian/* /usr/share/linda/* /var/cache/man/*  
  
RUN \  
curl -sL -o /usr/bin/jq
"https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64" && \  
chmod +x /usr/bin/jq  
  
RUN \  
curl -sL -o /usr/bin/cronexpr
"https://github.com/fentas/cronexpr/releases/download/0.1.0/cronexpr" && \  
chmod +x /usr/bin/cronexpr  
  
COPY maintain-replset.sh /usr/local/bin/maintain-replset.sh  
  
CMD ["/usr/local/bin/maintain-replset.sh"]  

