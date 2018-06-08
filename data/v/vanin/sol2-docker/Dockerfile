FROM debian:jessie-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
  
## Base requirements and upgrades  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
sudo \  
lsb-release \  
curl \  
git \  
make \  
g++ \  
libyaml-dev \  
ssh  
  
RUN apt-get dist-upgrade -y  
  
## Install PHP  
RUN apt-get update && apt-get install -y --no-install-recommends apt-
transport-https ca-certificates  
RUN curl -SLO https://packages.sury.org/php/apt.gpg && mv apt.gpg
/etc/apt/trusted.gpg.d/php.gpg  
RUN echo "deb https://packages.sury.org/php/ jessie main" >
/etc/apt/sources.list.d/php.list  
RUN apt-get update && apt-get install -y --no-install-recommends \  
php7.1 \  
php7.1-dom \  
php7.1-mbstring \  
php7.1-simplexml \  
php7.1-xml \  
php7.1-zip \  
php7.1-pdo \  
php7.1-tokenizer \  
php7.1-mysql \  
php7.1-sqlite3 \  
php7.1-curl \  
php7.1-mcrypt \  
php7.1-imagick \  
php7.1-gd \  
php7.1-xdebug \  
php7.1-apcu  
RUN apt-get purge -y php7.2-common  
RUN echo 'apc.enabled=1\n\  
apc.shm_size=64M\n\  
apc.ttl=7200\n\  
apc.mmap_file_mask=/tmp/apc.XXXXXX\n\  
apc.enable_cli=1' >> /etc/php/7.1/cli/conf.d/20-apcu.ini  
  
# Disable xdebug extension by default  
RUN rm /etc/php/7.1/cli/conf.d/20-xdebug.ini  
  
## Install Python  
RUN apt-get update && apt-get install -y --no-install-recommends python
python-dev python-pip  
  
## Install AWS CLI  
RUN pip install --upgrade awscli  
  
## Install Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
## Install Node.js  
RUN curl -SLO https://deb.nodesource.com/setup_8.x  
RUN bash setup_8.x && rm setup_8.x  
RUN apt-get update && apt-get install -y --no-install-recommends nodejs  
  
## Install Yarn  
RUN curl -SLO https://dl.yarnpkg.com/debian/pubkey.gpg  
RUN apt-key add pubkey.gpg  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y --no-install-recommends yarn  
  
## Install Dredd  
RUN npm install -g --progress=false -q --unsafe-perm dredd hercule  
  
## Install Apiary  
RUN apt-get install -y --no-install-recommends zlib1g-dev libssl-dev
libreadline-dev libgdbm-dev openssl  
RUN curl -SLO https://cache.ruby-lang.org/pub/ruby/stable/ruby-2.3.6.tar.gz;
tar xvfz ruby-2.3.6.tar.gz  
RUN cd ruby-2.3.6; sh configure; make; make install  
RUN gem install apiaryio  
  
## Install Docker  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
RUN echo "deb [arch=amd64] https://download.docker.com/linux/debian wheezy
stable"|tee /etc/apt/sources.list.d/docker.list  
RUN apt-get update && apt-get install -y --no-install-recommends docker-ce  
  
## Set timezone  
RUN ln -sf /usr/share/zoneinfo/Europe/Brussels /etc/localtime  
  
## Create user 'default'  
RUN useradd -ms /bin/bash default  
RUN usermod -aG sudo default  
RUN echo 'default ALL=(ALL) NOPASSWD:ALL' | EDITOR='tee -a' visudo  
RUN echo "default:default" | chpasswd  
USER default  
WORKDIR /home/default  
  
ENV PATH ${PATH}:vendor/bin:node_modules/.bin  
  
ENV DEBIAN_FRONTEND teletype  

