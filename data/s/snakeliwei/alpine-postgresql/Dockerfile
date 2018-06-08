FROM alpine:3.5  
RUN apk add --no-cache --update curl tzdata postgresql && \  
mkdir /docker-entrypoint-initdb.d && \  
curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64" && \  
chmod +x /usr/local/bin/gosu && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
apk del curl tzdata && \  
rm -rf /var/cache/apk/*  
  
ENV LANG C.UTF-8  
ENV PGDATA /var/lib/postgresql/data  
VOLUME /var/lib/postgresql/data  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

