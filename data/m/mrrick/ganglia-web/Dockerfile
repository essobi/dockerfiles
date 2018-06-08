FROM debian  
RUN apt-get update && apt-get install -y build-essential rsync  
COPY ganglia-web-3.7.4/ /ganglia-web/  
WORKDIR /ganglia-web/  
RUN make install  
  
FROM php:7-apache  
RUN apt-get update && apt-get install -y rrdtool  
COPY --from=0 /usr/share/ganglia-webfrontend/ /var/www/html/  
RUN mkdir -p /var/lib/ganglia/rrds && chown nobody /var/lib/ganglia/rrds && \  
mkdir -p /var/lib/ganglia-web/dwoo/compiled && mkdir -p /var/lib/ganglia-
web/dwoo/cache && \  
chown 33:33 -R /var/lib/ganglia-web/  

