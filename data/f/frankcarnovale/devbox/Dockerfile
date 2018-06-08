FROM centos:latest  
  
COPY builder.sh /  
COPY patches /patches  
COPY GO /usr/local/bin  
COPY devbox.sh /etc/profile.d  
  
RUN /builder.sh  
  

