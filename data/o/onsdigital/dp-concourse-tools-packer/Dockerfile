FROM williamyeh/ansible:alpine3  
  
RUN apk add --update bash curl gnupg gzip make git && rm -rf /var/cache/apk/*  
  
RUN curl
https://releases.hashicorp.com/packer/1.2.2/packer_1.2.2_linux_amd64.zip | \  
zcat > /usr/local/bin/packer && chmod +x /usr/local/bin/packer  

