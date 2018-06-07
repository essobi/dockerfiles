FROM jenkins/jenkins:lts-slim  
LABEL maintainer="Tobias Derksen <tobias.derksen@student.fontys.nl>"  
  
USER root  
  
# Install docker  
RUN rm /var/lib/apt/lists/* -vf && apt-get -y update && apt-get -y install
curl git sudo apt-transport-https ca-certificates curl gnupg2 software-
properties-common apt-utils nano \  
&& curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | sudo apt-key add - \  
&& add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(.
/etc/os-release; echo "$ID") $(lsb_release -cs) stable" \  
&& apt-get -y update \  
&& apt-get -y install docker-ce \  
&& curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-
compose-`uname -s`-`uname -m` -o /usr/bin/docker-compose \  
&& chmod +x /usr/bin/docker-compose \  
&& rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*  
  
# Install php, composer and phpunit  
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/sury.list \  
&& curl https://packages.sury.org/php/apt.gpg | apt-key add - \  
&& apt-get -y update \  
&& apt-get -y install php7.1-cli php7.1-common php7.1-curl php7.1-gd
php7.1-intl php7.1-json php7.1-mbstring php7.1-sqlite3 php7.1-mysql php7.1-xml
php-xdebug phpunit \  
&& php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');" \  
&& php /tmp/composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*  
  
# Install node, npm and yarn  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get -y update \  
&& apt-get -y install nodejs yarn \  
&& rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*  
  
RUN gpasswd -a jenkins docker && echo "jenkins ALL=NOPASSWD: ALL" >>
/etc/sudoers  
  
USER jenkins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt  
  
VOLUME /var/jenkins_home  

