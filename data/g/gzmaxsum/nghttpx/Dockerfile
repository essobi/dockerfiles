FROM alpine  
  
RUN apk add --no-cache nghttp2 python openssl ca-certificates libcap \  
&& setcap 'cap_net_bind_service=+ep' /usr/bin/nghttpx \  
&& apk del libcap  
  
ENTRYPOINT ["nghttpx"]  
CMD ["--conf=/data/conf/nghttpx.conf"]  

