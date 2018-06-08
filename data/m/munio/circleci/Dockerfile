FROM phpdockerio/php71-cli:latest  
  
# Disable interactive mode  
RUN echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/90circleci \  
&& echo 'DPkg::Options "--force-confnew";' >> /etc/apt/apt.conf.d/90circleci  
  
RUN apt-get update && apt-get install -y \  
git locales sudo openssh-client ca-certificates tar gzip parallel \  
net-tools netcat unzip zip bzip2 gnupg curl wget build-essential  
  
# set timezone to UTC by default  
RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime  
  
# use unicode  
RUN locale-gen en_US.UTF-8 || true  
ENV LANG=en_US.UTF-8  
# install jq  
RUN JQ_URL="https://circle-downloads.s3.amazonaws.com/circleci-
images/cache/linux-amd64/jq-latest" \  
&& curl --silent --show-error --location --fail --retry 3 --output /usr/bin/jq
$JQ_URL \  
&& chmod +x /usr/bin/jq \  
&& jq --version  
  
# install docker  
RUN set -ex \  
&& export DOCKER_VERSION=$(curl --silent --fail --retry 3
https://download.docker.com/linux/static/stable/x86_64/ | grep -o -e
'docker-[.0-9]*-ce\\.tgz' | sort -r | head -n 1) \  
&&
DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}"
\  
&& echo Docker URL: $DOCKER_URL \  
&& curl --silent --show-error --location --fail --retry 3 --output
/tmp/docker.tgz "${DOCKER_URL}" \  
&& ls -lha /tmp/docker.tgz \  
&& tar -xz -C /tmp -f /tmp/docker.tgz \  
&& mv /tmp/docker/* /usr/bin \  
&& rm -rf /tmp/docker /tmp/docker.tgz \  
&& which docker \  
&& (docker version || true)  
  
# install docker compose  
RUN COMPOSE_URL="https://circle-downloads.s3.amazonaws.com/circleci-
images/cache/linux-amd64/docker-compose-latest" \  
&& curl --silent --show-error --location --fail --retry 3 --output
/usr/bin/docker-compose $COMPOSE_URL \  
&& chmod +x /usr/bin/docker-compose \  
&& docker-compose version  
  
# install dockerize  
RUN DOCKERIZE_URL="https://circle-downloads.s3.amazonaws.com/circleci-
images/cache/linux-amd64/dockerize-latest.tar.gz" \  
&& curl --silent --show-error --location --fail --retry 3 --output
/tmp/dockerize-linux-amd64.tar.gz $DOCKERIZE_URL \  
&& tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64.tar.gz \  
&& rm -rf /tmp/dockerize-linux-amd64.tar.gz \  
&& dockerize --version  
  
# create circleci user  
RUN groupadd --gid 3434 circleci \  
&& useradd --uid 3434 --gid circleci --shell /bin/bash --create-home circleci
\  
&& echo 'circleci ALL=NOPASSWD: ALL' >> /etc/sudoers.d/50-circleci  
  
# install dependencies  
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y --no-install-recommends \  
nodejs yarn mysql-client \  
php7.1-bcmath php7.1-intl php7.1-mysql php7.1-sqlite3 php-redis php-imagick
php-xdebug  
  
# install composer  
RUN php -r
"copy('https://raw.githubusercontent.com/composer/getcomposer.org/master/web/installer',
'composer-setup.php');" \  
&& php composer-setup.php && php -r "unlink('composer-setup.php');" && mv
composer.phar /usr/local/bin/composer  
  
USER circleci  
  
CMD ["/bin/sh"]  

