FROM alpine:3.4  
  
ENV VERSION 0.9.6  
  
RUN apk update && \  
apk add ca-certificates curl \  
unzip \  
wget && \  
wget -q -O /terraform.zip
https://releases.hashicorp.com/terraform/${VERSION}/terraform_${VERSION}_linux_amd64.zip
&& \  
unzip /terraform.zip -d /bin && \  
find /bin -type f \  
-not -name 'busybox' \  
-not -name 'terraform' \  
-not -name 'terraform-provider-aws' \  
-not -name 'terraform-provider-terraform' \  
-exec rm {} \; && \  
apk del --purge wget unzip && \  
rm -rf /var/cache/apk/* /terraform.zip  
  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  

