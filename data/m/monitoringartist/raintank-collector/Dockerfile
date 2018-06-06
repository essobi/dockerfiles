FROM alpine  
MAINTAINER Jan Garaj info@monitoringartist.com  
  
ENV \  
RAINTANK_apiKey="" \  
RAINTANK_logLevel="ERROR" \  
RAINTANK_numCPUs=1 \  
RAINTANK_probeServerPort=8284 \  
RAINTANK_serverUrl="https://controller.raintank.io"  
  
COPY docker-image-files /  
  
RUN \  
export GOPATH=/go && \  
apk update && \  
apk add -f \  
g++ gcc make curl nodejs git go && \  
mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH" && \  
mkdir -p /opt/raintank && \  
cd /opt/raintank && \  
git clone https://github.com/raintank/raintank-collector.git && \  
# git clone -b loglevel https://github.com/jangaraj/raintank-collector && \  
go get github.com/raintank/raintank-probe && \  
cd raintank-collector && \  
cp $GOPATH/bin/raintank-probe . && \  
npm install && \  
chmod +x /bootstrap.sh && \  
apk del --purge g++ gcc make curl git go && \  
find . -name '*.md' -print -delete && \  
find . -name 'rfc*.txt' -print -delete && \  
find . -name 'LICENSE*' -print -delete && \  
find . -name '*.yml' -print -delete && \  
rm -rf ./node_modules/net-snmp/example && \  
rm -rf
./node_modules/cluster/node_modules/mkdirp/node_modules/minimist/example && \  
rm -rf ./node_modules/socket.io-client/node_modules/engine.io-
client/node_modules/xmlhttprequest-ssl/example && \  
rm -rf /var/cache/apk/* ${GOPATH} && \  
rm -rf /opt/raintank/raintank-collector/.git* /opt/raintank/raintank-
collector/.npmignore  
  
CMD ["/bootstrap.sh"]  

