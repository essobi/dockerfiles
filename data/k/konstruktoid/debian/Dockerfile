  
FROM scratch  
ADD ./stretch-1805152219.txz /  
ENV SHA256 a0b09cb5ece29a6dbb22dcb29c5e574ce441c070ab347582bba172d04b32ca91  
  
ARG TERM=linux  
ARG DEBIAN_FRONTEND=noninteractive  
  
ONBUILD RUN apt-get update && sh -c 'yes | apt-get --assume-yes upgrade'  
  

