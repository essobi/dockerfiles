FROM alpine:3.4  
RUN apk --update --no-cache add curl bash ca-certificates wget  
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub  
RUN wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk  
RUN apk add glibc-2.23-r3.apk  
RUN rm -rf /tmp/glibc-2.21-r2.apk /var/cache/apk/*  
  
ADD https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_linux_amd64.zip
/tmp/consul.zip  
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm
/tmp/consul.zip  
  
ADD https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_web_ui.zip
/tmp/webui.zip  
RUN mkdir /ui && cd /ui && unzip /tmp/webui.zip && rm /tmp/webui.zip  
RUN ls /ui  
  
ADD https://get.docker.io/builds/Linux/x86_64/docker-1.6.1 /bin/docker  
RUN chmod +x /bin/docker  
  
ADD ./config /config/  
ONBUILD ADD ./config /config/  
  
ADD ./start /bin/start  
ADD ./check-http /bin/check-http  
ADD ./check-cmd /bin/check-cmd  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53 53/udp  
VOLUME ["/data"]  
  
ENV SHELL /bin/bash  
  
ENTRYPOINT ["/bin/start"]  
CMD []  

