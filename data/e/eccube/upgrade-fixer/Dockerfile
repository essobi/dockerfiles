FROM php:7.1-cli  
  
MAINTAINER Kiy0taka Oku  
  
ADD https://github.com/EC-CUBE/Eccube-Upgrade-
Fixer/releases/download/v0.1.5-eccube-3.1.0-alpha/eccube-upgrade-fixer.phar
/usr/local/bin/eccube-upgrade-fixer  
RUN chmod +x /usr/local/bin/eccube-upgrade-fixer  
  
ENTRYPOINT ["eccube-upgrade-fixer"]  

