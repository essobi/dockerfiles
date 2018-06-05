FROM alpine  
  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
apk update && apk add curl "postgresql@edge<9.6" "postgresql-contrib@edge<9.6"
&& \  
mkdir /docker-entrypoint-initdb.d && \  
curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" && \  
chmod +x /usr/local/bin/gosu && \  
apk del curl && \  
rm -rf /var/cache/apk/*  
  
ENV LANG en_AU.utf8  
ENV PGDATA /var/lib/postgresql/data  
VOLUME /var/lib/postgresql/data  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

