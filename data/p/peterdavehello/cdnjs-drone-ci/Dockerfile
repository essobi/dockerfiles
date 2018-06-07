FROM node:8-alpine  
MAINTAINER Peter Dave Hello <hsu@peterdavehello.org>  
ENV NPM_CONFIG_LOGLEVEL warn  
RUN echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories && \  
apk -U upgrade && \  
apk -v add openssh-client rsync git@edge sshpass coreutils gawk openssl curl
ca-certificates jq && \  
rm -rf /var/cache/apk/*  
RUN ssh -V && \  
git --version && \  
node --version && \  
curl --version && \  
rsync --version && \  
jq --version  
RUN date > /date  
ADD cdnjs.sh /bin/  
ADD ColorEchoForShell/dist/ColorEcho.sh /  
ENTRYPOINT /bin/cdnjs.sh  

