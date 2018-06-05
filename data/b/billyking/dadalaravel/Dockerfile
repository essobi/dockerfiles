FROM node:latest  
RUN apt-get update  
RUN apt-get install -y net-tools vim wget git zsh build-essential php5
php5-sqlite php5-json nginx php5-fpm php5-cli php5-mcrypt net-tools php5-gd  
  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh  
RUN cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
RUN git clone git://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-
zsh/custom/plugins/zsh-syntax-highlighting  
  
RUN npm install -g bower  
RUN php -r "readfile('https://getcomposer.org/installer');" | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN composer global require "laravel/installer"  
ENV PATH $PATH:/root/.composer/vendor/bin  

