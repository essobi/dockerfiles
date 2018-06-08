FROM gliderlabs/alpine:3.3  
RUN apk -U add \  
bash \  
git \  
curl \  
netcat-openbsd \  
openssh-client  
  
RUN curl -L https://github.com/sequenceiq/docker-alpine-
dig/releases/download/v9.10.2/dig.tgz \  
|tar -xzv -C /usr/local/bin/  
  
RUN curl -L
https://github.com/lalyos/sigil/releases/download/v0.4.1/sigil_0.4.1_Linux_x86_64.tgz
\  
|tar -xzv -C /usr/local/bin/  
  
RUN curl -L
https://github.com/gliderlabs/glidergun/releases/download/v0.1.0/glidergun_0.1.0_Linux_x86_64.tgz
\  
|tar -xzv -C /usr/local/bin/  
  
CMD bash  

