FROM alpine:latest  
  
ENV MY_USERNAME=seiue  
ENV MY_PASSWD=seiue123  
  
RUN apk update && apk add --no-cache \  
bash coreutils util-linux tar which \  
make m4 findutils gawk sed grep less sudo shadow  
  
RUN echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
RUN useradd -m -u 1000 -g users -G wheel $MY_USERNAME  
RUN yes $MY_PASSWD | passwd $MY_USERNAME  
  
RUN apk update && apk add --no-cache \  
git jq the_silver_searcher \  
curl socat mariadb-client \  
neovim vim tmux  
  
RUN apk update && apk add --no-cache \  
php7 php7-pear php7-dev \  
php7-intl php7-openssl \  
php7-pdo php7-pdo_mysql \  
php7-pcntl php7-xsl php7-xml \  
php7-imagick php7-gd php7-fileinfo php7-mbstring \  
php7-apcu php7-json php7-iconv php7-curl php7-sysvshm \  
php7-zip php7-bcmath php7-sockets \  
php7-xmlwriter \  
php7-mcrypt \  
php7-ctype  
  
RUN curl -SL "https://getcomposer.org/composer.phar" -o
/usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer  
  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  

