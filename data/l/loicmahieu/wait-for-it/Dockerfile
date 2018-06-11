FROM ubuntu:16.04  
ENV WAITFORIT_VERSION="v1.3.2"  
RUN apt-get update && apt-get install -y curl \  
&& curl -o /usr/local/bin/waitforit -sSL
https://github.com/maxcnunes/waitforit/releases/download/$WAITFORIT_VERSION/waitforit-
linux_amd64 \  
&& chmod +x /usr/local/bin/waitforit \  
&& apt-get remove -y curl && apt-get -y autoremove && apt-get clean  
  
ENTRYPOINT ["/usr/local/bin/waitforit"]  

