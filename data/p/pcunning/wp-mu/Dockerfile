FROM tutum/apache-php:latest  
MAINTAINER Borja Burgos <borja@tutum.co>, Feng Honglin <hfeng@tutum.co>  
  
WORKDIR /  
RUN apt-get update && \  
apt-get -yq install mysql-client curl && \  
rm -rf /app && \  
curl -0L http://wordpress.org/latest.tar.gz | tar zxv && \  
mv /wordpress /app && \  
rm -rf /var/lib/apt/lists/*  
  
RUN sed -i "s/AllowOverride None/AllowOverride All/g"
/etc/apache2/apache2.conf  
RUN a2enmod rewrite  
ADD wp-config.php /app/wp-config.php  
ADD htaccess /app/.htaccess  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
# Expose environment variables  
ENV DB_HOST **LinkMe**  
ENV DB_PORT **LinkMe**  
ENV DB_NAME wordpress  
ENV DB_USER admin  
ENV DB_PASS **ChangeMe**  
  
EXPOSE 80  
VOLUME ["/app/wp-content"]  
CMD ["/run.sh"]  

