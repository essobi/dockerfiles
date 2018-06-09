FROM ubuntu:trusty  
  
MAINTAINER Shapovalov Alexandr <alex_sh@kodeks.ru>  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
#####################################  
# Non-Root User:  
#####################################  
# Add a non-root user to prevent files being created with root permissions on
host machine.  
ARG PUID=1000  
ARG PGID=1000  
RUN groupadd -g $PGID workspace && \  
useradd -u $PUID -g workspace -m workspace  
  
#####################################  
# Set Timezone  
#####################################  
ARG TZ=UTC  
ENV TZ ${TZ}  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Install "software-properties-common" (for the "add-apt-repository")  
RUN apt-get update && apt-get install -y \  
software-properties-common  
  
#####################################  
# Setup PHP  
#####################################  
# Add the "PHP 7" ppa  
RUN add-apt-repository -y \  
ppa:ondrej/php  
  
# Install PHP-CLI 7, some PHP extentions and some useful Tools with APT  
RUN apt-get update && apt-get install -y --force-yes \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-json \  
php7.0-xml \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-sqlite \  
php7.0-sqlite3 \  
php7.0-zip \  
php7.0-memcached \  
php7.0-tidy \  
sqlite3 \  
libsqlite3-dev \  
git \  
curl \  
vim \  
nano \  
nodejs \  
nodejs-dev \  
npm \  
zsh  
  
#####################################  
# ZSH  
#####################################  
COPY .zshrc /home/workspace/  
RUN chown workspace: /home/workspace/.zshrc  
  
USER workspace  
#RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)"  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh  
RUN git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-
zsh/custom/themes/powerlevel9k  
  
# Add an alias for PHPUnit  
RUN echo "alias phpunit='./vendor/bin/phpunit'" >> ~/.zshrc  
  
#####################################  
# NodeJS  
#####################################  
USER root  
# Add a symbolic link for Node  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install gulp and bower with NPM  
RUN npm install -g \  
gulp \  
bower \  
n  
  
RUN n 5.10.0  
  
# Clean up  
USER root  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#####################################  
# Install Composer  
#####################################  
USER root  
RUN curl -s http://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN usermod -aG sudo workspace  
RUN sed -i 's/\%sudo.*/\%sudo ALL=(ALL) NOPASSWD:ALL/g' /etc/sudoers  
  
USER workspace  
RUN /usr/local/bin/composer global require "hirak/prestissimo:^0.2"  
  
#zsh as shell  
RUN sudo chsh -s /usr/bin/zsh workspace  
  
WORKDIR /var/www  
CMD ["su", "-", "workspace", "-c", "/usr/bin/zsh"]  

