# docker build -t medialon/asset-distribution:3.0.1 -t medialon/asset-
distribution:latest .  
FROM busybox  
  
RUN mkdir -p /dist  
  
#copy the assets  
RUN mkdir -p /dist/assets  
COPY assets /dist/assets  
  
# copy the initial db data dump  
RUN mkdir -p /dist/database  
COPY database /dist/database  
  
#copy the default config dist  
COPY server.cfg /dist/server.cfg  

