FROM alpine  
  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& apk add --no-cache oath-toolkit-oathtool  
  
ENTRYPOINT [ "/usr/bin/oathtool" ]  

