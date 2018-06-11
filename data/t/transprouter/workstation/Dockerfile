FROM alpine:latest  
RUN apk add --no-cache --quiet shadow iptables openssh-client curl  
RUN useradd -m direct -s /bin/sh \  
&& useradd -m transprouter -s /bin/sh  
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["transprouter"]  

