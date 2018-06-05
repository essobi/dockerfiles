FROM nginx:1.10.2  
ADD web.nginx.conf /etc/nginx/conf.d/default.conf  
ADD init.sh /root/init.sh  
RUN chmod 0700 /root/init.sh  
  
RUN mkdir /backups  
  
VOLUME /backups  
  
EXPOSE 80  
CMD ["/root/init.sh"]  

