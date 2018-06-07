FROM ubuntu:14.04.3  
RUN apt-get -y update  
RUN apt-get install -y apache2  
RUN apt-get install -y unzip  
  
WORKDIR /data  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 80  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["apache"]  

