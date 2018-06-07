FROM alpine  
  
EXPOSE 8080  
ENV PGWEB_VERSION 0.9.12  
ENV DB_HOST postgres  
ENV DB_PORT 5432  
ENV DB_DATABASE postgres  
ENV DB_USER postgres  
ENV DB_PASSWORD postgres  
ENV DB_SSL disable  
  
RUN \  
apk update && \  
apk add --update ca-certificates openssl && \  
update-ca-certificates && \  
cd /tmp && \  
wget
https://github.com/sosedoff/pgweb/releases/download/v$PGWEB_VERSION/pgweb_linux_amd64.zip
&& \  
unzip pgweb_linux_amd64.zip -d /usr/bin && \  
mv /usr/bin/pgweb_linux_amd64 /usr/bin/pgweb && \  
rm -f pgweb_linux_amd64.zip  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

