FROM alpine  
  
MAINTAINER 興怡  
ARG VNC_PASSWORD=secret  
ENV VNC_PASSWORD ${VNC_PASSWORD}  
ENV GOPATH /home/alpine/go  
  
RUN echo "http://dl-3.alpinelinux.org/alpine/edge/testing"
>>/etc/apk/repositories \  
&& apk --no-cache add \  
x11vnc xvfb supervisor sudo \  
dwm dmenu ii st \  
ttf-ubuntu-font-family \  
&& addgroup alpine \  
&& adduser -G alpine -s /bin/ash -D alpine \  
&& echo "alpine:alpine" | /usr/sbin/chpasswd \  
&& echo "alpine ALL=(ALL) ALL" >> /etc/sudoers \  
&& rm -rf /apk /tmp/* /var/cache/apk/* \  
&& mkdir -p /etc/supervisor/conf.d \  
&& x11vnc -storepasswd $VNC_PASSWORD /etc/vncsecret \  
&& chmod 444 /etc/vncsecret  
  
COPY supervisord.conf /etc/supervisor/conf.d  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  
  
WORKDIR /home/alpine  
EXPOSE 5900  

