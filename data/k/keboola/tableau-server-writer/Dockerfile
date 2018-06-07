FROM keboola/base-php56  
MAINTAINER Jakub Matejka <jakub@keboola.com>  
  
WORKDIR /home  
  
# Initialize  
RUN git clone https://github.com/keboola/tableau-server-writer.git ./  
RUN git checkout tags/1.1.3  
RUN composer install --no-interaction  
  
ENTRYPOINT php ./src/run.php --data=/data

