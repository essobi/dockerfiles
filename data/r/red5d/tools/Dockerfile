FROM alpine:latest  
  
MAINTAINER Red5d  
  
# A lightweight image with some common commandline tools that I use.  
  
RUN apk add \--no-cache build-base python3 python3-dev libxml2-dev libxslt-dev
mtr git openssh speedtest-cli nmap nmap-scripts && \  
pip3 install \--upgrade pip && pip3 install requests ptpython csvkit howdoi &&
\  
nmap --script-updatedb && \  
apk del build-base python3-dev  

