FROM debian:jessie  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gdal-bin \  
postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /output  
WORKDIR /usr/src/app  
COPY ./ /usr/src/app  
CMD ["./export-geojson.sh"]  

