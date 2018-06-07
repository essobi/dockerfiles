FROM php:latest  
  
# Update and Install Packages  
RUN apt-get update -y && apt-get install -y \  
ant \  
curl \  
git \  
libc-client-dev \  
libcurl4-gnutls-dev \  
libfreetype6-dev \  
libkrb5-dev \  
libxslt1-dev \  
libxslt1.1 \  
openssh-client \  
unzip \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install PHP Modules  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \  
docker-php-ext-install -j$(nproc) \  
bcmath \  
curl \  
gd \  
imap \  
json \  
xsl \  
zip  
  
# Install Composer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer \  
&& rm /tmp/composer-setup.php  
  
# Disable host key checking from within builds as we cannot interactively
accept them  
# TODO: It might be a better idea to bake ~/.ssh/known_hosts into the
container  
RUN mkdir -p ~/.ssh  
RUN printf "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config  
  

