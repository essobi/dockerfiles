FROM alpine:3.3  
COPY files.txt /tmp/  
  
# install packer (with only selected components)  
RUN apk add --update ca-certificates curl openssl unzip && \  
curl -L -o /tmp/packer.zip \  
https://releases.hashicorp.com/packer/0.8.6/packer_0.8.6_linux_amd64.zip && \  
openssl dgst -sha256 /tmp/packer.zip \  
| grep '2f1ca794e51de831ace30792ab0886aca516bf6b407f6027e816ba7ca79703b5' \  
|| (echo 'shasum mismatch' && false) && \  
unzip /tmp/packer.zip -d /tmp/packer && \  
mkdir -p /opt/packer && \  
xargs -I % cp /tmp/packer/% /opt/packer < /tmp/files.txt && \  
ln -s /opt/packer/packer /usr/local/bin/packer && \  
rm -rf /tmp/* /var/cache/apk/*  
  
CMD ["packer", "--help"]  

