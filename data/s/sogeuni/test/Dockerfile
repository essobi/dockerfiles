FROM armhf/alpine  
  
COPY qemu-arm /usr/bin/qemu-arm-static  
  
RUN ["/usr/bin/qemu-arm-static", "/bin/sh", "-c", "/bin/echo Hello from ARM
container"]  
  
RUN apk add --update git  

