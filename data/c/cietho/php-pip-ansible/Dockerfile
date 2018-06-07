FROM php:7.1.1  
  
RUN apt-get update && apt-get install -y ssh libffi-dev python-dev libssl-dev
rsync python-pip python-setuptools && \  
docker-php-ext-install bcmath && \  
docker-php-ext-install zip && \  
pip install -U pip setuptools && \  
pip install ansible  

