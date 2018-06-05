FROM mongo:2.6  
  
EXPOSE 28017  
  
CMD mongod \--bind_ip 0.0.0.0 \--logpath /data/db/mongodb.log \--logappend
\--rest \--httpinterface \--auth

