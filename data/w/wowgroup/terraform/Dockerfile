FROM alpine:3.3  
MAINTAINER WOW! Group Development  
  
RUN apk -Uv add ca-certificates zip mysql-client \  
&& update-ca-certificates \  
&& wget -O /tmp/terraform.zip
https://releases.hashicorp.com/terraform/0.11.5/terraform_0.11.5_linux_amd64.zip
\  
&& unzip /tmp/terraform.zip -d /usr/local/bin \  
&& mkdir -p /workspace \  
&& rm -rf /tmp/terraform.zip /var/cache/apk/*  
  
ADD bin/terraform-provider-fleet /usr/local/bin/  
ADD .terraformrc /root/  
ADD runner /  
WORKDIR /workspace  
ENTRYPOINT ["/runner"]  

