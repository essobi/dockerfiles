FROM alpine:3.7  
LABEL maintainer="quentin.mcgaw@gmail.com" \  
description="Update the IP address of one or more of your records of one or
more GoDaddy domain(s) every 5 minutes." \  
download="3.3MB" \  
size="9.6MB" \  
ram="6MB" \  
cpu_usage="Very low" \  
github="https://github.com/qdm12/godaddy-ip-ddns"  
COPY entrypoint.sh /  
RUN apk add -q --progress --update --no-cache curl bash ca-certificates && \  
rm -rf /var/cache/apk/* && \  
chmod +x /entrypoint.sh  
ENV TARGETS= \  
KEY= \  
SECRET= \  
DELAY=300  
HEALTHCHECK \--interval=7m --timeout=5s --start-period=7s --retries=3 \  
CMD [ $(ping -q -c 1 "$(echo ${TARGETS:2:${#TARGETS}} | cut -d, -f1)" | grep
-m 1 PING | cut -d "(" -f2 | cut -d ")" -f1) == $(wget -qO- -T 2
https://ipinfo.io/ip) ] || exit 1  
ENTRYPOINT /entrypoint.sh

