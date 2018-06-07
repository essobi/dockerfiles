FROM gliderlabs/alpine:3.4  
ENV RANCHER_CLI_VERSION 0.4.1  
ADD
https://github.com/rancher/cli/releases/download/v${RANCHER_CLI_VERSION}/rancher-
linux-amd64-v${RANCHER_CLI_VERSION}.tar.gz /tmp/  
  
RUN \  
apk --update add ca-certificates && \  
cd /tmp && \  
tar xvfz rancher-linux-amd64-v${RANCHER_CLI_VERSION}.tar.gz && \  
cp rancher-v${RANCHER_CLI_VERSION}/rancher /usr/bin/rancher && \  
rm -rf rancher* && \  
chmod +x /usr/bin/rancher  
  
CMD ["/bin/sh"]

