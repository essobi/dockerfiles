from php:cli  
MAINTAINER Nicolas Potier <nicolas.potier@acseo-conseil.fr>  
  
RUN mkdir -p /tmp/staging  
RUN apt-get -qq update && apt-get -qq install -y wget libbz2-dev git  
RUN docker-php-ext-install bz2  
RUN wget http://get.sensiolabs.org/php-cs-fixer.phar -O /tmp/php-cs-fixer &&
chmod a+x /tmp/php-cs-fixer  
RUN wget -c http://static.phpmd.org/php/latest/phpmd.phar -O /tmp/phpmd &&
chmod a+x /tmp/phpmd  
RUN wget -nv --no-check-certificate
https://gitlab.acseo.co/acseoteam/phpmd_ruleset/raw/master/phpmd-last-
commit.sh -O /tmp/phpmd-last-commit && chmod a+x /tmp/phpmd-last-commit  
RUN wget
https://gitlab.acseo.co/acseoteam/phpmd_ruleset/raw/master/ruleset.xml -O
/tmp/ruleset.xml >/dev/null 2>&1  

