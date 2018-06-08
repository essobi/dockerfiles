# This Dockerfile contains scripts to deploy to rancher  
FROM alpine:3.5  
RUN apk --no-cache update && \  
apk --no-cache add ca-certificates sudo bash wget unzip make coreutils curl &&
\  
update-ca-certificates && \  
rm -rf /var/cache/apk/*  
RUN wget https://github.com/amaysim-au/build_scripts/archive/master.zip -O
build-scripts.zip && \  
unzip -o build-scripts.zip && \  
mv build_scripts-master/* /usr/local/bin  
RUN wget -qO- https://github.com/rancher/cli/releases/download/v0.2.0/rancher-
linux-amd64-v0.2.0.tar.gz | tar xz && \  
mv ./rancher-v0.2.0/rancher /usr/local/bin/rancher  
CMD bash

