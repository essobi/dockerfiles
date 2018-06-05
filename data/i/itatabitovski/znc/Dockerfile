FROM itatabitovski/alpine:3.5  
ENV ZNC_VERSION 1.6.4-r0  
  
RUN apk-install znc=$ZNC_VERSION \  
znc-extra=$ZNC_VERSION  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/bin/znc"]  

