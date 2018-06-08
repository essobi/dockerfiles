FROM debian:latest  
  
MAINTAINER Romain THERRAT <romain@pockost.com>  
  
RUN apt-get update && apt-get install -y jpegoptim --no-install-recommends &&
rm -r /var/lib/apt/lists/*  
  
# Set up the application directory  
VOLUME ["/app"]  
WORKDIR /app  
  
ENTRYPOINT ["jpegoptim"]  
CMD [ "-h" ]  

