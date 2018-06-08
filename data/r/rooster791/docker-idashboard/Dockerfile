FROM eboraas/apache-php  
RUN apt-get update && apt-get -y install git  
RUN rm -rf /var/www/html  
RUN git clone https://github.com/causefx/iDashboard-PHP /var/www/html  
RUN chmod -R 777 /var/www/html  
EXPOSE 80  
VOLUME /var/www/html  
COPY ./scripts/* /scripts/  
  
RUN chmod +x /scripts/*  
  
CMD ["/scripts/boot.sh"]  

