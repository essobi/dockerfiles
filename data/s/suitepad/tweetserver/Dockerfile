FROM nginx  
  
RUN apt-get update && \  
apt-get install -y curl && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /etc/nginx/conf.d  
ADD ./run /usr/sbin/run  
RUN chmod +x /usr/sbin/run  
  
CMD run  

