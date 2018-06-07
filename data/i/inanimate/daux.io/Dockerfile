FROM tutum/apache-php  
  
EXPOSE 80  
# Download the daux.io archive on github  
ADD http://github.com/justinwalsh/daux.io/archive/master.tar.gz /var/www/html/  
WORKDIR /var/www/html  
  
# Untar the archive  
RUN tar xvf master.tar.gz -C /var/www/html && rm master.tar.gz  
RUN cp -r daux.io-master/* /var/www/html/  
RUN rm -rf /var/www/html/daux.io-master  
  
# Setup apache  
RUN a2enmod rewrite  
RUN rm -rf /etc/apache2/sites-enabled/*  
COPY daux.io.conf /etc/apache2/sites-enabled/daux.io.conf  
  
# Copy custom config.json  
COPY config.json /var/www/html/docs/  

