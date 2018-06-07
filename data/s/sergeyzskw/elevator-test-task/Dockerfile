FROM php:7.0-cli  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /home/composer/.composer  
  
RUN apt-get update && \  
apt-get install -y git-all ssh-client zip unzip && \  
docker-php-ext-install -j$(nproc) bcmath && \  
rm -r /var/lib/apt/lists/*  
  
# Install composer  
RUN php -r "readfile('https://getcomposer.org/installer');" | php --
--install-dir /usr/local/bin --filename composer && \  
mkdir -p /home/composer/.composer && \  
ln -s /root/.ssh /home/composer/.ssh  
  
COPY id_rsa-elevator_test_task-github.com /root/.ssh/id_rsa  
COPY known_hosts /root/.ssh/known_hosts  
  
RUN chmod 600 /root/.ssh/id_rsa && \  
cd /opt && \  
git clone git@github.com:sergey-zsk/elevator-test-task.git  
  
COPY parameters.yml /opt/elevator-test-task/app/config/parameters.yml  
  
RUN cd /opt && \  
cd /opt/elevator-test-task/ && \  
composer install  
  
RUN apt-get update && \  
apt-get purge -y git-all && \  
apt-get autoremove -y && \  
rm -r /var/lib/apt/lists/*  
  
WORKDIR /opt/elevator-test-task  
CMD ["bin/console","elevator:emulate"]  
  

