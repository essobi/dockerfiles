FROM golang:latest  
RUN mkdir -p /opt/whatsrunning/data  
  
COPY whatsrunning /opt/whatsrunning/  
COPY templates /opt/whatsrunning/templates  
COPY dist /opt/whatsrunning/dist  
COPY config.json /opt/whatsrunning/  
  
EXPOSE 8080  
WORKDIR /opt/whatsrunning/  
VOLUME /opt/whatsrunning/data  
  
ENTRYPOINT ["./whatsrunning"]  

