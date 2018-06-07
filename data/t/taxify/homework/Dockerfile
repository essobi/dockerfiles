FROM mysql:5.6.35  
ENV MYSQL_ALLOW_EMPTY_PASSWORD true  
  
#only patch is required for DB, all the rest are for backend (they are
together to optimize image size)  
RUN apt-get update && apt-get -y install patch curl apt-transport-https bzip2
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
-  
RUN echo 'deb https://deb.nodesource.com/node_4.x jessie main' >
/etc/apt/sources.list.d/nodesource.list  
  
RUN apt-get update && apt-mark hold mysql-server && apt-get -y install nodejs
libfontconfig && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /data  
VOLUME ["/data"]  
  
EXPOSE 80  
EXPOSE 8000-8999  

