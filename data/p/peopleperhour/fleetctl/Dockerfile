FROM gliderlabs/alpine:3.3  
MAINTAINER Panagiotis Moustafellos <pmoust@peopleperhour.com>  
  
ENV VERSION 0.11.8  
ENV FLEETCTL_ENDPOINT http://127.0.0.1:2379  
RUN apk-install curl && \  
curl -LOks
https://github.com/coreos/fleet/releases/download/v${VERSION}/fleet-v${VERSION}-linux-
amd64.tar.gz && \  
tar zxvf fleet-v${VERSION}-linux-amd64.tar.gz && \  
cp fleet-v${VERSION}-linux-amd64/fleetctl /fleetctl && \  
rm -rf fleet-v* && \  
chmod +x /fleetctl  
  
ENTRYPOINT ["/fleetctl"]  

