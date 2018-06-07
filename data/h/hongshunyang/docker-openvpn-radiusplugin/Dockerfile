FROM hongshunyang/docker-openvpn  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
## update openvpn 2.3.14  
## update openvpn 2.3.14 with xor  
  
RUN apk add -U libgcrypt libstdc++ \  
&& apk add -U --virtual build-deps build-base libgcrypt-dev git \  
&& cd /tmp/ \  
&& git clone -b production --single-branch
https://hongshunyang@bitbucket.org/hongshunyang/openvpn-radiusplugin.git \  
&& cd openvpn-radiusplugin \  
&& make \  
&& cp radiusplugin.so /usr/lib/openvpn/plugins/ \  
&& apk del -U build-deps \  
&& cd ~ \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  

