FROM alpine:edge  
  
RUN echo @testing http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& apk add --no-cache nginx-naxsi@testing \  
&& mkdir -p /run/nginx # dir for .pid  
  
CMD ["nginx", "-g", "daemon off;"]  

