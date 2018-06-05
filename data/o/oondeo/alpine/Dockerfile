FROM alpine:edge  
  
ADD scripts/* /usr/local/bin/  
  
#Use dash instead busybox  
#edge repository breaks installs  
#RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
RUN chmod +x /usr/local/bin/* && \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk add --no-cache tini && \  
apk add --no-cache dash@testing && cp /usr/bin/dash /bin/sh && ln -s
/bin/busybox /sh && mkdir -p /app /etc/skel  
  
ADD localtime /etc/localtime  
  
VOLUME /etc/skel  
  
WORKDIR /app  
  
ENTRYPOINT ["/sbin/tini", "-g" ,"--", "/usr/local/bin/start.sh"]  
  
CMD [ "/sh" ]  

