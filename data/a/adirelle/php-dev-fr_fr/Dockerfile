FROM adirelle/debian-fr_fr  
MAINTAINER adirelle+docker@gmail.com  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends php5-cli php5-intl php5-json
php5-mcrypt php5-pgsql php5-xsl php5-twig \  
php5-curl php5-ldap php5-xdebug php5-apcu ca-certificates less vim-common man
sudo postgresql-client git \  
&& rm /etc/php5/cli/conf.d/*-xdebug.ini  
  

