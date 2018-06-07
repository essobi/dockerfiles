FROM ubuntu:trusty  
MAINTAINER Elliott Peay <elliott.peay@gmail.com>  
  
# The basics  
RUN apt-get update && \  
apt-get -y install php5-cli vim  
  
# Get Composer  
RUN php -r "readfile('https://getcomposer.org/installer');" \  
| php -- \--filename=composer \--install-dir=/usr/bin  
  
# Make our app user  
RUN useradd appuser  
  
RUN mkdir /app  
WORKDIR /app  
  
ADD ./ ./  
  
RUN chown -R appuser:appuser ./  
  
USER appuser  
  
RUN composer install  
  
EXPOSE 8000  
CMD ["./app-run"]  
  

