# OVS Docker image  
FROM alpine:3.7  
LABEL maintainer "Cisco Contiv (https://contiv.github.io)"  
  
RUN mkdir -p /etc/openvswitch /var/log/contiv \  
&& echo 'http://dl-cdn.alpinelinux.org/alpine/v3.4/main' >>
/etc/apk/repositories \  
&& apk --no-cache add \  
openvswitch=2.5.0-r0 iptables ca-certificates openssl curl bash  
  
COPY ovsInit.sh /scripts/  
  
ENTRYPOINT ["/scripts/ovsInit.sh"]  

