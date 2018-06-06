FROM alpine:3.6  
RUN apk add --update \  
curl \  
&& curl -SLO
https://github.com/containernetworking/plugins/releases/download/v0.7.0/cni-
plugins-amd64-v0.7.0.tgz \  
&& tar xvfpz cni-plugins-amd64-v0.7.0.tgz  
  
ENTRYPOINT ["./dhcp", "daemon", "-hostprefix", "/host"]  

