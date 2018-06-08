FROM oopartners/php  
  
RUN apt-get update  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs git  
RUN npm install -g bower  
RUN npm install -g gulp  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
  
VOLUME ["/u"]  

