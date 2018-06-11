FROM gliderlabs/alpine  
MAINTAINER Oded Lazar <oded@senexx.com>  
  
# install needed dependencies  
RUN apk update && apk upgrade && \  
apk-install curl bash tree  
  
# download the latest jq release  
RUN curl -sL "https://api.github.com/repos/stedolan/jq/releases/latest" | \  
awk -F '"' '/browser.*jq-linux64/ { print $4 }' | \  
xargs curl -Lo /bin/jq && \  
chmod 755 /bin/jq  
  
RUN adduser -S vault  
  
ADD unseal.sh /home/vault/unseal.sh  
RUN chmod 755 /home/vault/unseal.sh  
  
USER vault  
WORKDIR "/home/vault"  
CMD ["bash", "unseal.sh", "keys"]  

