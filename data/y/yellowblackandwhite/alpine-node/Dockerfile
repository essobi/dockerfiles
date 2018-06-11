FROM yellowblackandwhite/alpine-base  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
RUN echo http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories
&& \  
apk add --no-cache curl bash git make gcc g++ python linux-headers \  
paxctl libgcc libstdc++ file autoconf automake nasm gnupg nodejs nodejs-dev  
USER alpine  

