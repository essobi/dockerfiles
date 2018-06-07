FROM alpine:3.6  
RUN apk update \  
&& apk add --no-cache \  
openvpn \  
; \  
rm -rf /var/lib/apk/* /var/cache/apk/*  
  
VOLUME /etc/openvpn  
WORKDIR /etc/openvpn  
  
ENTRYPOINT [ \  
"/usr/sbin/openvpn", \  
"--config", \  
"/etc/openvpn/openvpn.conf" \  
]  

