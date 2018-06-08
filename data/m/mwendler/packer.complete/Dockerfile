# a minimal packer setup based on alpine  
#  
FROM alpine  
MAINTAINER Mike  
  
ENV PACKER_VERSION 0.8.6  
# download and install Packer.  
RUN mkdir /tmp/packer \  
&& cd /tmp/packer \  
&& apk add --update curl ca-certificates \  
\  
&& echo 'installing packer ...' \  
&& curl -O -sS -L
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
\  
&& unzip packer_${PACKER_VERSION}_linux_amd64.zip \  
&& mv packer* /usr/local/bin \  
\  
&& echo 'cleaning up ... ' \  
&& apk del unzip \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/packer \  
&& rm -rf packer_${PACKER_VERSION}_linux_amd64.zip \  
&& rm -rf /usr/local/bin/packer_${PACKER_VERSION}_linux_amd64.zip  
  
# define a mount point for the data to use  
VOLUME /data  
WORKDIR /data  
  
# define default command.  
CMD ["packer"]  

