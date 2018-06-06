FROM alpine:3.7  
RUN apk --no-cache add ca-certificates && \  
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O
/usr/local/bin/cloud_sql_proxy && \  
chmod +x /usr/local/bin/cloud_sql_proxy  
  
ENTRYPOINT ["cloud_sql_proxy"]  
CMD ["--help"]  

