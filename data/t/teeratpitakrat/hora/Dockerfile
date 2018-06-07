FROM alpine  
  
ADD config.toml /config.toml  
ADD https://github.com/teeratpitakrat/hora/releases/download/v0.0.3/hora-
linux-amd64 /hora  
RUN chmod 755 /hora  
  
EXPOSE 8080  
CMD ["/hora"]  

