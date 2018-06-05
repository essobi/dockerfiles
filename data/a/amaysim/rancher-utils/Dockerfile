# This Dockerfile contains scripts to deploy to rancher  
FROM alpine:3.5  
ENV RANCHER_CLI_URL
https://github.com/rancher/cli/releases/download/v0.6.0-rc3/rancher-linux-
amd64-v0.6.0-rc3.tar.xz  
RUN apk --no-cache update && \  
apk --no-cache add ca-certificates sudo bash wget unzip make coreutils curl &&
\  
update-ca-certificates && \  
rm -rf /var/cache/apk/*  
RUN wget -qO- $RANCHER_CLI_URL | tar xvJ && \  
mv ./rancher-v0.6.0-rc3/rancher /usr/local/bin/rancher  
ADD scripts /scripts  
RUN chmod a+x /scripts/*.sh && chmod a+x /scripts/libs/*.sh  
CMD ["rancher", "--version"]

