FROM alpine:3.5  
RUN apk add --no-cache asciidoc openjdk8-jre-base curl && \  
curl -o /tmp/fop.tar.gz
http://ftp.unicamp.br/pub/apache/xmlgraphics/fop/binaries/fop-2.1-bin.tar.gz
&& \  
tar -zxC /usr/local/ -f /tmp/fop.tar.gz && \  
rm /tmp/fop.tar.gz && \  
ln -s /usr/local/fop-2.1/fop /usr/bin/fop  
  
WORKDIR /workdir  
ENTRYPOINT ["/usr/bin/a2x"]  

