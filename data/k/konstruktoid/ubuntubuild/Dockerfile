  
FROM scratch  
ADD ./bionic-1805152200.txz /  
ENV SHA256 1e7dbe61620e52418aa8ff25bcea2a1fb8864dfb42ad9e2460fde3f0232944ba  
  
ARG TERM=linux  
ARG DEBIAN_FRONTEND=noninteractive  
  
ONBUILD RUN apt-get update && sh -c 'yes | apt-get --assume-yes upgrade'  
  

