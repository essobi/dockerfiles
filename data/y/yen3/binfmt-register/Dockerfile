FROM alpine  
  
WORKDIR /qemu  
  
RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/community/
\  
\--virtual .qemu-static-binaries qemu-arm qemu-aarch64 \  
&& cp -fa /usr/bin/qemu-arm /qemu/qemu-arm-static \  
&& cp -fa /usr/bin/qemu-aarch64 /qemu/qemu-aarch64-static \  
&& apk del .qemu-static-binaries  
  
COPY ./qemu-binfmt-register.sh .  
COPY ./start.sh .  
  
ENTRYPOINT ["/qemu/start.sh"]  
  

