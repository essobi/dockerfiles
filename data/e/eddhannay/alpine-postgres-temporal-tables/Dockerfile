FROM gliderlabs/alpine:3.4  
COPY docker-entrypoint.sh /  
  
ENV LANG en_US.utf8  
ENV PGDATA /var/lib/postgresql/data  
VOLUME /var/lib/postgresql/data  
  
RUN apk-install gcc musl-dev py-pip make postgresql-dev "postgresql-contrib"
postgresql curl && \  
mkdir /docker-entrypoint-initdb.d && \  
curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" && \  
chmod +x /usr/local/bin/gosu && \  
chmod +x /docker-entrypoint.sh && \  
pip install pgxnclient && \  
su - postgres && \  
pgxnclient install temporal_tables && \  
apk del gcc musl-dev make postgresql-dev curl py-pip && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

