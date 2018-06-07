FROM alpine:latest  
MAINTAINER J. Elfring <devops@elfrinjo.de>  
  
RUN apk --no-cache add \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/community \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/main \  
tor  
  
COPY ./assets/torrc.relay /etc/tor/torrc.relay  
COPY ./assets/entrypoint.sh /etc/tor/entrypoint.sh  
  
RUN chown -R tor /etc/tor &&\  
chmod 755 /etc/tor/entrypoint.sh  
  
ENV TOR_NICK="Landesverrat" \  
TOR_CONTACT="Not Provided" \  
TOR_BRIDGE=0  
VOLUME /var/lib/tor  
  
# tor port as defined in torrc  
EXPOSE 9001 9030  
USER tor  
ENTRYPOINT [ "/etc/tor/entrypoint.sh" ]  

