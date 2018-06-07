FROM ubuntu:16.04  
RUN apt-get update -qq && apt-get install -y wget php libapache2-mod-php php-
mcrypt php-mysql sshpass php-curl composer nodejs npm php-mbstring php-dom
php-zip  
  
ADD http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar /usr/local/bin/php-
cs-fixer  
RUN chmod a+x /usr/local/bin/php-cs-fixer  
  
COPY ./foobar.sh /usr/local/bin/foobar  
RUN chmod a+x /usr/local/bin/foobar  

