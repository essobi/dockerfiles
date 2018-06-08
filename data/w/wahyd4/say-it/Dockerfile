FROM golang:1.8-alpine3.6  
# RUN apt-get update && apt-get install -y ca-certificates  
COPY say-it-backend /root/  
  
EXPOSE 8080  
CMD chmod +x /root/say-it-backend  
  
ENTRYPOINT /root/say-it-backend  
  

