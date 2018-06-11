FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
libssl1.0.0  
  
# Copy and unzip to /utserver  
ADD utserver.tar.gz /utserver  
COPY utserver.conf /utserver/utorrent-server-alpha-v3_3/  
  
# WebUI Port  
EXPOSE 8080  
# BitTorrent protocol port  
EXPOSE 6881  
VOLUME /data  
  
WORKDIR /utserver/utorrent-server-alpha-v3_3/  
ENTRYPOINT ["./utserver", "-configfile", "utserver.conf", "-logfile",
"/var/log/utserver.log"]  
  

