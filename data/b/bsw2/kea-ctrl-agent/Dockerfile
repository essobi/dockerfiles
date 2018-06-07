FROM alpine:3.7  
COPY brian.woolstrum@gmail.com-5a7691ec.rsa.pub /etc/apk/keys  
RUN sed -i '$ ahttp://alpine.woolstrum.net/testing\n' /etc/apk/repositories  
RUN apk update && \  
apk add --no-cache kea-ctrl-agent  
  
RUN sed -i "s,/tmp/kea-dhcp4-ctrl.sock,/var/kea/kea/kea-dhcp4-ctrl.sock,g"
/etc/kea/kea-*.conf  
RUN sed -i "s,127.0.0.1,0.0.0.0,g" /etc/kea/kea-ctrl-agent.conf  
#RUN mkdir /originals && cp /etc/kea/kea-ctrl-agent.conf /originals  
VOLUME /var/kea/kea  
VOLUME /etc/kea  
  
EXPOSE 8080  
CMD ["/usr/sbin/kea-ctrl-agent","-c","/etc/kea/kea-ctrl-agent.conf"]  

