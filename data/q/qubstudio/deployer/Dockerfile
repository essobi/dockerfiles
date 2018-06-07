FROM php:7.1.6-cli  
  
MAINTAINER kuzyk <andriy.kuzyk@qubstudio.com>  
  
RUN apt-get update && apt-get install apt-transport-https -y  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" >>
/etc/apt/sources.list.d/yarn.list  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
  
RUN apt-get install -y \  
libpng-dev \  
openssh-client \  
curl \  
wget \  
zip \  
rsync \  
unzip \  
nodejs \  
git \  
yarn  
  
RUN echo "export PATH=$PATH:`yarn global bin`" >> ~/.bashrc  
  
RUN yarn global add gulp  
  
RUN curl https://getcomposer.org/composer.phar -Ls --output /usr/bin/composer  
RUN chmod +x /usr/bin/composer  
  
RUN curl https://deployer.org/deployer.phar -Ls --output /usr/bin/deployer  
RUN chmod +x /usr/bin/deployer  
  
ENTRYPOINT ["deployer", "composer"]  
  
CMD ["--version"]

