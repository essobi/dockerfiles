FROM wrfly/alpine-mysql:latest  
COPY e.sh /  
RUN sed -i "s/dl-cdn.alpinelinux.org/alpine.cdn.h3llo.cn/"
/etc/apk/repositories && \  
chmod +x /e.sh  
CMD ["/e.sh"]

