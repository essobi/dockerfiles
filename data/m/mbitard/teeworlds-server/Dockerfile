FROM debian:jessie  
  
RUN DEBIAN_FRONTEND=noniteractive && \  
apt-get update && \  
apt-get install -y lib32z1 lib32stdc++6 && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD teeworlds_files /teeworlds  
  
EXPOSE 8303/udp 8304/udp 8305/udp  
WORKDIR /teeworlds  
CMD ["/teeworlds/teeworlds_insta","-f", "conf"]  

