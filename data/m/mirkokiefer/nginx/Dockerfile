  
FROM mirkokiefer/ubuntu-base  
  
RUN echo deb http://archive.ubuntu.com/ubuntu precise main universe >
/etc/apt/sources.list  
RUN echo deb http://archive.ubuntu.com/ubuntu precise-updates main universe >>
/etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y nginx  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN rm /etc/nginx/sites-enabled/default  
  
ADD nginx-site.conf /etc/nginx/sites-enabled/default  
  
RUN mkdir -p /data/www  
  
# Expose ports  
EXPOSE 80  
CMD service nginx start  

