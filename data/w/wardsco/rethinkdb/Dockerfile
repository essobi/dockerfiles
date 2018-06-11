FROM alpine:edge  
  
WORKDIR /data  
VOLUME ["/data"]  
# process, cluster, webui  
EXPOSE 28015 29015 8080  
ENTRYPOINT ["rethinkdb"]  
CMD ["--bind", "all"]  
  
RUN apk add --no-cache rethinkdb  

