FROM alpine:3.7  
ENV USER aptsync  
ENV UID 1000  
ENV TZ Asia/Shanghai  
  
RUN apk add --update --no-cache gzip xz bzip2 tzdata perl su-exec wget curl
ca-certificates && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo
"Asia/Shanghai" > /etc/timezone  
  
COPY apt-mirror /usr/bin/  
COPY mirror.list /etc/apt/mirror.list  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apt-mirror"]  
  

