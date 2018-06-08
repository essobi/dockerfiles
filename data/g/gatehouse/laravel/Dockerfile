FROM php:7.1.1  
## install and configure laravel dependencies  
ADD bootstrap.sh /usr/local/bin/bootstrap  
RUN chmod +x /usr/local/bin/bootstrap  
RUN bootstrap  
  
## set up script for pipelines to deploy results to build server  
ADD deploy.sh /usr/local/bin/deploy  
RUN chmod +x /usr/local/bin/deploy  
  
## set up script for pipelines to run migrations  
ADD migrate.sh /usr/local/bin/migrate  
RUN chmod +x /usr/local/bin/migrate  

