FROM alpine  
MAINTAINER Philippe Lafoucrière <philippe.lafoucriere@tech-angels.com>  
  
ENV BATS_VERSION 0.4.0  
RUN apk add --update bash curl docker && \  
curl -o "/tmp/v${BATS_VERSION}.tar.gz" -L
"https://github.com/sstephenson/bats/archive/v${BATS_VERSION}.tar.gz" && \  
tar -x -z -f "/tmp/v${BATS_VERSION}.tar.gz" -C /tmp/ && \  
bash "/tmp/bats-${BATS_VERSION}/install.sh" /usr/local && \  
rm -rf /tmp/* /var/cache/apk/*  
  
ENTRYPOINT ["/usr/local/bin/bats"]  
CMD ["-h"]  

