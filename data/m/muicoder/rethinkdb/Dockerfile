FROM muicoder/glibc:alpine  
  
RUN apk add --no-cache rethinkdb rethinkdb-doc  
  
VOLUME ["/rethinkdb_data"]  
  
CMD ["rethinkdb", "--bind", "all"]  
  
EXPOSE 28015 29015 8080  

