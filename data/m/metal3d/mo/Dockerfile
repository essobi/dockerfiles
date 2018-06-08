FROM alpine:latest  
MAINTAINER Patrice FERLET <metal3d@gmail.com>  
  
RUN set -ex;\  
cd /tmp;\  
apk add --update git bash ;\  
git clone https://github.com/tests-always-included/mo.git;\  
cd mo;\  
mv mo /usr/local/bin/mo; \  
chmod +x /usr/local/bin/mo; \  
cd /tmp; \  
rm -rf mo; \  
apk del git;\  
rm -rf /var/cache/apk/*;  
  
WORKDIR /opt  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/mo"]  

