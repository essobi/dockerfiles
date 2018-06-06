FROM tutum/lamp:latest  
  
  
RUN apt-get update && apt-get install -y wget \  
unzip  
  
RUN rm -rf /app  
RUN wget -O bWAPP_latest.zip http://github.com/dannystdu/bwapp-
custom/archive/master.zip  
RUN wget http://github.com/dannystdu/bwapp-custom/archive/master.zip \  
&& unzip master.zip \  
&& cd bwapp-custom-master \  
&& mv bWAPP /app  
  
RUN sed -i 's/db_password = "bug"/db_password = ""/g' /app/admin/settings.php  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
RUN chmod -R 777 /var/www/html/passwords  
  
EXPOSE 80 3306  
ENTRYPOINT ["/run.sh"]  

