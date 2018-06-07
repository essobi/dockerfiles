FROM viur/viur-vpc  
MAINTAINER http://www.viur.is  
WORKDIR /src  
ADD . .  
  
RUN cp /src/scripts/getapp /usr/bin/getapp && \  
chmod 755 /usr/bin/getapp && \  
cp /src/scripts/vc_start.sh /usr/bin/vc_start && \  
chmod +x /usr/bin/vc_start  
  
VOLUME ["/Projects"]  
  
EXPOSE 5000 8000 8080  
CMD ["/usr/bin/vc_start"]  

