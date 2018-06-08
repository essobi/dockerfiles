FROM alpine:edge  
  
RUN echo "http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --update --no-cache bash sane-saned sane-utils sane-backend-epson
sane-backend-epson2 busybox-extras && \  
echo "6566 stream tcp nowait root.root /usr/sbin/saned saned" >/etc/inetd.conf
&& \  
addgroup saned lp  
  
ADD https://raw.githubusercontent.com/jpetazzo/pipework/master/pipework
/pipework  
ADD run.sh /run.sh  
  
EXPOSE 631  
EXPOSE 5353/udp  
  
ENV ALLOW_HOSTS="192.168.1.0/24 172.17.0.1/24"  
CMD /run.sh  

