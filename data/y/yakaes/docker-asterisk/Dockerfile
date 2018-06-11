FROM alpine  
  
RUN \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk --no-cache add \  
asterisk vorbis-tools@community  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["server"]  
  

