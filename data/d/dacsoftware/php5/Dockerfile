FROM ubuntu:14.04  
WORKDIR /root  
  
RUN mkdir .ssh  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV CI 1  
RUN apt-get update && apt-get install -y software-properties-common ssh build-
essential  
RUN ssh-keyscan bitbucket.org > /root/.ssh/known_hosts  
  
# LIBS  
RUN apt-get install -y curl git libmcrypt-dev libicu-dev libxslt-dev
libxml2-dev unzip libfontconfig  
  
# PHP  
RUN add-apt-repository -y ppa:ondrej/php  
RUN apt-get update && apt-get install -y php5.6  
  
# PHP Extensions  
RUN apt-get install -y php5.6-mbstring php5.6-mcrypt php5.6-curl \  
php5.6-intl php5.6-bcmath php5.6-xml php5.6-xsl php5.6-zip php5.6-pgsql
php5.6-redis  
  
# Composer  
ADD install_composer.sh ./install_composer.sh  
RUN ./install_composer.sh  
RUN mv composer.phar /usr/local/bin/composer  
RUN rm install_composer.sh  
  
# PRESTISSIMO (to increase composer performance)  
RUN composer global require "hirak/prestissimo:^0.3"  
  
# NODE JS  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
COPY npmrc .npmrc  
  
# YARN  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y yarn  
  
# BUILD TOOLS  
RUN npm install -g grunt-cli bower  
  
# POSTGRES  
RUN apt-get install -y postgresql postgresql-contrib postgresql-9.3-plproxy
postgresql-plperl-9.3 postgresql-plpython-9.3 \  
postgresql-pltcl-9.3  
RUN service postgresql start && cd /tmp && sudo -H -u postgres psql template1
-c 'CREATE EXTENSION hstore' && sudo service postgresql restart  
  
# REDIS  
RUN apt-get install -y redis-server  
  
COPY pg_hba.conf /etc/postgresql/9.3/main  

