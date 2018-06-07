FROM alpine:3.7  
MAINTAINER frederic.cabestre [at] easymile.com  
  
COPY Easymile-Root-Certificate-Authority-G1.crt /usr/local/share/ca-
certificates/  
  
RUN apk add --no-cache --update \  
ca-certificates=20171114-r0 \  
libcrypto1.0=1.0.2n-r0 \  
openssl=1.0.2n-r0 \  
ncurses-libs=6.0_p20170930-r0 \  
bash=4.4.12-r2 \  
jq=1.5-r4 \  
curl=7.57.0-r0 && \  
rm -rf /var/cache/apk/* && \  
update-ca-certificates  
  
ENTRYPOINT ["/release/bin/boot"]  

