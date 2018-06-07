FROM busybox  
MAINTAINER falms <F@L.fal.ms>  
  
EXPOSE 80  
COPY dumb-init_1.2.0_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
CMD ["dumb-init", "tail", "-f", "/dev/null"]  

