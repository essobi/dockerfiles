FROM debian:latest  
  
RUN apt-get update && apt-get install -y optipng --no-install-recommends && rm
-r /var/lib/apt/lists/*  
  
# Set up the application directory  
VOLUME ["/app"]  
WORKDIR /app  
  
ENTRYPOINT ["optipng"]  
CMD [ "-h" ]  

