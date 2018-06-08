FROM alpine:3.5  
LABEL maintainer "rimelek@rimelek.hu"  
  
RUN apk update && apk add openssh-client \  
&& echo -e 'Host *\nUseRoaming no' >> /etc/ssh/ssh_config  
  
ENV TUNNEL_PORT_MIN=2000 \  
TUNNEL_PORT_MAX="" \  
TUNNEL_HOST=""  
COPY start-ssh-tunnel.sh /start.sh  
  
RUN chmod +x /start.sh  
  
ENTRYPOINT []  
  
CMD ["/bin/sh", "-c", "/start.sh"]  
  

