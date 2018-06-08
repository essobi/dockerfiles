FROM debian:jessie  
  
# Install packages  
RUN apt-get -y update \  
&& apt-get install -y \  
mumble-server \  
&& rm -rf /var/lib/apt/lists/*  
  
# Default config  
RUN mkdir /mnt/data \  
&& cp /etc/mumble-server.ini /mnt/data/murmur.ini \  
&& sed -i -e "s:^database=.*$:database=/mnt/data/murmur.sqlite:"
/mnt/data/murmur.ini \  
&& sed -i -e "s:^logfile=.*$:logfile=:" /mnt/data/murmur.ini \  
&& sed -i -e "s:^port=.*$:port=64738:" /mnt/data/murmur.ini \  
&& chown -R mumble-server:mumble-server /mnt/data  
  
VOLUME /mnt/data  
  
EXPOSE 64738  
USER mumble-server  
CMD murmurd -fg -ini /mnt/data/murmur.ini  

