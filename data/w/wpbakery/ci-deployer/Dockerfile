FROM php:5.6-cli  
  
RUN apt-get update \  
&& apt-get install -y wget ssh  
  
RUN wget http://deployer.org/deployer.phar \  
&& chmod +x deployer.phar \  
&& mv deployer.phar /usr/local/bin/dep  

