FROM alpine  
MAINTAINER Victor Castell <victor@victorcastell.com>  
  
ENV DKRON_VERSION 0.10.2  
RUN set -x \  
&& buildDeps='bash ca-certificates openssl' \  
&& apk add --update $buildDeps \  
&& rm -rf /var/cache/apk/* \  
&& mkdir -p /opt/local/dkron \  
&& wget -O dkron.tar.gz
https://github.com/victorcoder/dkron/releases/download/v${DKRON_VERSION}/dkron_${DKRON_VERSION}_linux_amd64.tar.gz
\  
&& tar -xzf dkron.tar.gz \  
&& mv dkron_${DKRON_VERSION}_linux_amd64/* /opt/local/dkron \  
&& rm dkron.tar.gz \  
&& rm -rf dkron_${DKRON_VERSION}_linux_amd64  
  
EXPOSE 8080 8946  
ENV SHELL /bin/bash  
WORKDIR /opt/local/dkron  
  
ENTRYPOINT ["/opt/local/dkron/dkron"]  
  
CMD ["--help"]  

