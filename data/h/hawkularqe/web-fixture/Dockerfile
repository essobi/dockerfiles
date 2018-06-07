FROM nginx  
  
ENV CRON_EXP=*  
ENV DURATION=5m  
  
RUN apt-get update && apt-get install -y cron && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /var/www/html  
  
COPY conf/custom_http_code.conf /etc/nginx/conf.d/  
COPY sh/docker_start.sh /usr/bin/docker_start.sh  
COPY html/index.html /var/www/html/  
  
EXPOSE 8080  
CMD ["/usr/bin/docker_start.sh"]  

