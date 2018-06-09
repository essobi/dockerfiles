# Generated automatically by update.sh  
# Do no edit this file  
FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install --yes --no-install-recommends \  
texlive \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /app  
WORKDIR /app  
  
CMD ["pdftex"]  

