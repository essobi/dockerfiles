FROM sylvaindeloux/php-front:7.1-cli  
MAINTAINER Sylvain Deloux <docker@eax.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN cd /root && \  
wget https://github.com/deployphp/deployer/archive/v4.3.0.zip -O deployer.zip
&& \  
unzip deployer.zip && \  
rm deployer.zip && \  
mv deployer-4.3.0 deployer  
  
RUN cd /root/deployer && \  
composer install  
  
ENTRYPOINT ["/root/deployer/bin/dep"]  

