FROM debian:jessie-slim  
RUN apt-get update && apt-get install -y --force-yes samba vim \  
&& apt-get autoremove -y -qq \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

