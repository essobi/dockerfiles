FROM tutum/apache-php  
MAINTAINER Nicolas Ritouet <nicolas@ritouet.com>  
  
EXPOSE 80  
# Download the daux.io archive on github  
ADD http://github.com/justinwalsh/daux.io/archive/master.tar.gz /var/www/html/  
WORKDIR /var/www/html  
  
# Untar the archive  
RUN tar xvf master.tar.gz -C /var/www/html && rm master.tar.gz  
RUN cp -r daux.io-master/* /var/www/html/  
RUN rm -rf /var/www/html/daux.io-master  
  
# Copy custom config.json  
COPY config.json /var/www/html/docs/  

