#  
# Dockerfile for shadowsocks-libev and kcptun  
#  
FROM tofuliang/docker-shadowsocks-libev:latest  
MAINTAINER tofuliang@gmail.com  
  
ENV ARUKAS_TOKEN=  
ENV ARUKAS_SECERT=  
ENV ARUKAS_CHECK_FEQ 40  
ENV GLOBAL_PROXY=true  
  
COPY client.sh /usr/local/bin/client.sh  
RUN set -ex \  
&& apk add --no-cache wget jq sshpass \  
&& chmod a+x /usr/local/bin/client.sh  
  
CMD /usr/local/bin/client.sh  

