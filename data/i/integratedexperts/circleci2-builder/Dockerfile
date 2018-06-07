FROM php:7.1-cli  
  
# Install git and ssh.  
RUN apt-get update -qq \  
&& apt-get install -y git ssh zip unzip vim lynx curl  
  
# Install docker.  
RUN curl -L -o /tmp/docker-17.03.0-ce.tgz
https://get.docker.com/builds/Linux/x86_64/docker-17.03.0-ce.tgz \  
&& tar -xz -C /tmp -f /tmp/docker-17.03.0-ce.tgz \  
&& mv /tmp/docker/* /usr/bin  
  
# Install docker-compose.  
RUN curl -L https://github.com/docker/compose/releases/download/1.11.2/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
# Install composer.  
ENV COMPOSER_ALLOW_SUPERUSER=1  
RUN curl -L -o /usr/local/bin/composer
https://getcomposer.org/download/1.6.3/composer.phar \  
&& echo "52cb7bbbaee720471e3b34c8ae6db53a38f0b759c06078a80080db739e4dcab6
/usr/local/bin/composer" | sha256sum \  
&& chmod +x /usr/local/bin/composer  
  
# Install composer plugin to speed up packages downloading.  
RUN composer global require hirak/prestissimo  
  
# Install NVM and NodeJS.  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.29.0/install.sh | bash  
ENV NVM_DIR=/root/.nvm  
ENV SHIPPABLE_NODE_VERSION=v8.9.1  
RUN . $HOME/.nvm/nvm.sh \  
&& nvm install $SHIPPABLE_NODE_VERSION \  
&& nvm alias default $SHIPPABLE_NODE_VERSION \  
&& nvm use default  
ENV PATH $NVM_DIR/versions/node/$SHIPPABLE_NODE_VERSION/bin:$PATH  

