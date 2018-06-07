FROM alpine:latest  
  
# Install curl  
RUN apk add --update curl  
  
# Launch script that runs updater and loops  
COPY launch.sh /  
ENTRYPOINT ["/launch.sh"]  

