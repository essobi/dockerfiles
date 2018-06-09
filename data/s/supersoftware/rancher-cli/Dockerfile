FROM alpine:3.6  
  
ENV CLI_VERSION v0.6.4  
  
RUN apk add --update ca-certificates openssl && update-ca-certificates && \  
mkdir /cli && cd /cli && \  
wget -qO-
https://github.com/rancher/cli/releases/download/${CLI_VERSION}/rancher-linux-
amd64-${CLI_VERSION}.tar.gz | tar xvz && \  
mv rancher-${CLI_VERSION}/rancher /bin/. && \  
cd / && \  
rm -rf /cli && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["rancher"]  

