FROM debian:jessie  
  
RUN apt-get update && apt-get install --assume-yes --no-install-recommends \  
r-base  
  
COPY Rprofile.site /etc/R/  
  
ENTRYPOINT ["R"]  

