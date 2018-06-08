FROM karllhughes/laravel-php-7  
MAINTAINER Nick Cousins <nick@rightrevenue.co.uk>  
  
RUN unset COMPOSER_HOME  
RUN locale-gen en_GB.utf8 && update-locale  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update && apt-get install -qy git curl libmcrypt-dev mysql-client
zip unzip nodejs php-apigen  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && pip
install awsebcli awscli --upgrade  
  
CMD /bin/bash  

