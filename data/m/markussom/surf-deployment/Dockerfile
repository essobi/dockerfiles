FROM php:7.0  
RUN apt-get update && \  
apt-get install -y openssh-server openssl && \  
apt-get clean  
  
RUN curl -L -o surf.phar
https://github.com/TYPO3/Surf/releases/download/2.0.0-beta7/surf.phar && \  
mv surf.phar /usr/local/bin/surf && \  
chmod +x /usr/local/bin/surf  

