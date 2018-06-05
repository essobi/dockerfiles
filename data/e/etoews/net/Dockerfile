FROM alpine  
  
RUN apk update && apk add \  
curl \  
jq \  
nmap \  
ca-certificates \  
python \  
py-pip \  
&& rm -rf /var/cache/apk/* \  
&& pip install httpie httpie-unixsocket  
  
CMD ["/bin/sh"]  

