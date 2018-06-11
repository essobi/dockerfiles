FROM alpine:edge  
  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
  
RUN apk add --no-cache rspamd=1.5.0-r0 rmilter=1.10.0-r0  
  
RUN mkdir /run/rspamd /run/rmilter  
  
ADD rspamd-wrapper.sh /  
  
ENTRYPOINT ["/rspamd-wrapper.sh"]  

