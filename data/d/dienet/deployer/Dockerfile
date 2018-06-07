FROM debian:stable  
  
EXPOSE 4500  
  
ADD . /app/src/github.com/die-net/deployer  
  
ENTRYPOINT ["/app/bin/deployer"]  
  
RUN apt-get -q update && \  
apt-get -y -q dist-upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y -q --no-install-recommends
ca-certificates curl git build-essential && \  
apt-get clean && \  
mkdir -p /usr/local/go /app/pkg /app/bin && \  
curl -sS https://storage.googleapis.com/golang/go1.9.2.linux-amd64.tar.gz | \  
tar --strip-components=1 -C /usr/local/go -xzf - && \  
GOPATH=/app /usr/local/go/bin/go get github.com/die-net/deployer && \  
rm -rf /usr/local/go /app/pkg && \  
apt-get -y -q remove git build-essential && \  
apt-get -y -q autoremove  

