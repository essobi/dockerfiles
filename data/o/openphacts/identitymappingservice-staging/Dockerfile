FROM mysql:5.6  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y wget
axel cpipe  
  
ADD download.sh staging.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*.sh  
  
RUN mkdir /download  
WORKDIR /download  
RUN mkdir /staging  
RUN /usr/local/bin/download.sh && mv /download/*.sql.gz /staging/ims.sql.gz  
VOLUME /staging  
  
CMD ["/usr/local/bin/staging.sh"]  
  

