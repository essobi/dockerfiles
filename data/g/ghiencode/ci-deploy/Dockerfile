FROM ubuntu:xenial  
  
RUN apt-get update -qq && apt-get install -yqq \  
apt-transport-https \  
ca-certificates \  
curl \  
language-pack-en-base \  
lxc \  
software-properties-common \  
&& set -x \  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add \- \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu xenial stable" \  
&& LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install docker-ce -yqq \  
&& docker -v \  
&& curl -s -L https://github.com/docker/compose/releases/latest | \  
egrep -o '/docker/compose/releases/download/[0-9.]*/docker-compose-
Linux-x86_64' | \  
wget --base=http://github.com/ -i - -O /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& /usr/local/bin/docker-compose --version \  
&& apt-get update -qq \  
&& apt-get install -qqy php7.1-cli php7.1-mbstring php7.1-soap php7.1-curl
php7.1-mongodb php7.1-gd php7.1-mcrypt php7.1-bcmath php7.1-mysql
php7.1-sqlite3 php7.1-xml libmcrypt-dev libicu-dev libxml2-dev libssl-dev curl
git-core unzip python2.7 jq g++ python-software-properties libfontconfig
build-essential ruby-dev nodejs gettext default-jre default-jdk \  
&& apt-get clean -qqy \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer global require phpunit/phpunit:* \  
&& composer global require phing/phing:* \  
&& ln -s ~/.composer/vendor/bin/phpunit /usr/local/bin/phpunit \  
&& ln -s ~/.composer/vendor/bin/phing /usr/local/bin/phing \  
&& curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& mkdir -p ~/.ssh \  
&& echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config  

