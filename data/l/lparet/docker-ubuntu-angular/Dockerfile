FROM lparet/docker-ubuntu-apache2:1.2  
## Configure apt and install softwares  
RUN apt-get -y update \  
&& LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl \  
&& curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get -y update \  
&& LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y \  
software-properties-common \  
build-essential \  
libssl-dev \  
nodejs \  
yarn \  
&& apt-get clean \  
&& rm -fr /var/cache/apt/ \  
&& rm -rf /var/lib/apt/lists/*  
  
## Install AngularCli  
RUN yarn global add @angular/cli  
  
## Activate rewrite : .htaccess will override Apache conf  
RUN a2enmod rewrite  
  
## Add files  
ADD ./config/ /  
  
ADD Dockerfile /Dockerfile  
  
## Run entrypoint : npm install + ng build  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["supervisord","-c","/etc/supervisord.conf"]

