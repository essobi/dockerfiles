FROM mongo:3.6.2  
COPY export/* /export/  
COPY scripts/import_mongo.sh /docker-entrypoint-initdb.d/  
CMD ["mongod"]  

