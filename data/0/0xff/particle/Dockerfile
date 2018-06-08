FROM ubuntu:artful  
  
## dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --force-yes -y -o
Dpkg::Options::="--force-confnew" \  
php7.1 php7.1-cli php7.1-mbstring php7.1-json php7.1-xml python ca-
certificates openssl build-essential \  
curl wget zip git apt-transport-https lsb-release sudo libfontconfig bzip2 &&
\  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && sudo apt-get install
-y nodejs && npm --no-color install -g npm-run-all && \  
curl --silent --show-error https://getcomposer.org/installer | php && mv
composer.phar /usr/local/bin/composer && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
## warm up npm and composer  
ADD ./package.json ./package-lock.json /src/  
ADD ./apps/pl/pattern-lab/composer.* /src/apps/pl/pattern-lab/  
WORKDIR /src  
RUN npm --no-color install && COMPOSER_NO_INTERACTION=1 npm --no-color run
setup  
  
## test 'n build just for shits 'n giggles  
ADD . /src  
RUN npm --no-color run lint && npm --no-color run test && npm --no-color run
build:pl  
CMD npm --no-color start  
EXPOSE 8080  
## badge  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL \  
org.label-schema.name="particle" \  
org.label-schema.url="https://hub.docker.com/r/0xff/particle/" \  
org.label-schema.vcs-url="https://github.com/piccaso/particle" \  
org.label-schema.schema-version="1.0"  

