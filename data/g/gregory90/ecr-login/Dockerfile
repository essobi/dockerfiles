FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -y python3-pip  
RUN pip3 install awscli  
  
RUN mkdir -p /app  
RUN mkdir -p /data  
ADD run /app/run  
RUN chmod +x /app/run  
  
ENTRYPOINT ["/app/run"]  
  

