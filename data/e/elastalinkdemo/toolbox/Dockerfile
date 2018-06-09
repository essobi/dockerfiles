FROM ubuntu:16.10  
  
USER root  
  
RUN apt-get update && apt-get install -y curl \  
&& curl -sL https://deb.nodesource.com/setup_7.x | bash \  
&& apt install -y nodejs \  
&& npm install npm@4.0.3 -g \  
&& npm install -g less \  
&& apt-get install -y php-mongodb composer vim less curl mysql-client \  
&& apt-get clean \  
&& rm -Rf /var/lib/apt/lists/*  
  
ENTRYPOINT []  
  

