FROM gliderlabs/alpine:3.1  
MAINTAINER lajos.papp@sequenceiq.com  
  
RUN apk-install curl  
  
RUN curl -Lko /tmp/terra.zip
https://releases.hashicorp.com/terraform/0.6.9/terraform_0.6.9_linux_amd64.zip
\  
&& cd /usr/local/bin \  
&& unzip /tmp/terra.zip \  
&& rm -rf /tmp/terra.zip  
  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["/usr/local/bin/terraform"]  

