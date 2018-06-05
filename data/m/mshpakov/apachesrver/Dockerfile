FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y \  
git \  
curl \  
cron \  
wget \  
zsh \  
nano \  
apache2 \  
php7.0 \  
php7.0-fpm \  
php7.0-cli \  
php7.0-curl \  
php7.0-zip \  
php7.0-json \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-mcrypt \  
php7.0-mbstring \  
php7.0-gd \  
php7.0-xml  
  
RUN apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean  
  
# Install Zsh  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && cp
~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
RUN sed -i "s/robbyrussell/af-magic/" ~/.zshrc  
RUN echo TERM=xterm >> /root/.zshrc  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Add certbot  
# https://certbot.eff.org/  
RUN wget -P /usr/sbin/ https://dl.eff.org/certbot-auto  
RUN chmod a+x /usr/sbin/certbot-auto  
  
RUN chown -R root:root /etc/cron.d  
RUN chmod -R 0644 /etc/cron.d  
  
# Install GS to downgrade pdf files  
RUN apt-get update && apt-get -y install ghostscript && apt-get clean  

