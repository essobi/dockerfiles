FROM alpine:latest  
  
#Install mongodb  
RUN apk add --no-cache mongodb && \  
rm /usr/bin/mongoperf  
  
# Create the MongoDB data directory  
RUN mkdir -p /data/db  
  
# Expose port 27017 and 27018 from the container to the host  
EXPOSE 27017 27018  
# Set /usr/bin/mongod as the entry-point  
ENTRYPOINT ["/usr/bin/mongod"]

