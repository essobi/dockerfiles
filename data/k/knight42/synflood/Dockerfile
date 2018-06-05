FROM alpine:edge  
ENTRYPOINT ["bash"]  
LABEL maintainer "Jian Zeng <anonymousknight96@gmail.com>"  
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing/' >>
/etc/apk/repositories && \  
apk add --no-cache -U --allow-untrusted iproute2 nginx bmon tcpdump curl bash
hping3  
ADD synflood.c /  
RUN apk add --no-cache -U --virtual build gcc musl-dev && gcc -D_GNU_SOURCE -o
/synflood synflood.c && apk del build  

