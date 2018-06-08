################################################################################  
# Base image  
################################################################################  
  
FROM noriaas/composer:latest  
  
MAINTAINER Billy Nguyen <billy.nguyen@noria.no>  
  
################################################################################  
# Build instructions  
################################################################################  
  
ENV DEFAULT_APP_USER=noria \  
DEFAULT_APP_GROUP=noria \  
DEFAULT_APP_UID=1000 \  
DEFAULT_APP_GID=1000  
  
# Install packages  
RUN \  
set -ex; \  
apk add --no-cache gosu python; \  
  
  
mkdir -p /packagist; \  
cd /packagist; \  
  
git clone https://github.com/hirak/packagist-crawler ./; \  
composer install; \  
curl https://bootstrap.pypa.io/get-pip.py -o - | python; \  
pip install supervisor supervisor-stdout  
  
  
WORKDIR /packagist  
VOLUME /packagist/cache  
  
ADD ./docker-entrypoint.sh /  
ADD ./supervisor.conf /etc/packagist.conf  
ADD ./config.php /packagist  
ADD ./index.html.php /packagist  
ADD https://raw.githubusercontent.com/rmm5t/jquery-
timeago/master/jquery.timeago.js /packagist  
  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

