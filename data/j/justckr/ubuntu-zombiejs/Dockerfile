FROM justckr/ubuntu-base:latest  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && apt-get install -y -q --no-install-recommends \  
php7.0-* \  
nodejs \  
&& apt-get -y remove php7.0-snmp \  
&& rm -rf /var/lib/apt/lists/*  
ENV PATH /app/src/vendor/bin:$PATH  
RUN npm install zombie --save-dev  

