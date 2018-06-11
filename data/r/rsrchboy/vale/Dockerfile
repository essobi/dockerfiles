# Chris Weyl <cweyl@alumni.drew.edu> 2017  
FROM alpine:3.6  
MAINTAINER Chris Weyl <cweyl@alumni.drew.edu>  
  
RUN apk update && \  
apk add wget ca-certificates && \  
wget -O vale.tgz
https://github.com/ValeLint/vale/releases/download/0.9.0/vale_0.9.0_Linux_64-bit.tar.gz
&& \  
tar -zxvf vale.tgz && mv vale /bin && \  
rm -rf /var/cache  
  
ENTRYPOINT [ "vale" ]  

