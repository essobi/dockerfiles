FROM alpine:latest  
MAINTAINER Charlie Wang <272876047@qq.com>  
  
RUN apk add --update openssh util-linux dbus ttf-freefont xauth xf86-input-
keyboard sudo\  
&& rm -rf /tmp/* /var/cache/apk/*  
RUN addgroup alpine \  
&& adduser -G alpine -s /bin/sh -D alpine \  
&& echo "alpine:alpine" | /usr/sbin/chpasswd \  
&& echo "alpine ALL=(ALL) ALL" >> /etc/sudoers  
  
ADD docker-entrypoint.sh /usr/sbin  
RUN chmod +x /usr/sbin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["/usr/sbin/sshd","-D"]  

