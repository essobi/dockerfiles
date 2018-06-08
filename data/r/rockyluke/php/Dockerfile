# Copyright (c) 2016, rockyluke  
#  
# Permission to use, copy, modify, and/or distribute this software for any  
# purpose with or without fee is hereby granted, provided that the above  
# copyright notice and this permission notice appear in all copies.  
#  
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH  
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY  
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,  
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM  
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR  
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR  
# PERFORMANCE OF THIS SOFTWARE.  
FROM rockyluke/debian:jessie  
MAINTAINER rockyluke  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq && \  
apt-get upgrade -qq -y  
  
# get composer (http://getcomposer.org/)  
RUN curl -Ls -o /usr/local/bin/composer.phar
https://getcomposer.org/composer.phar && \  
chmod 755 /usr/local/bin/composer.phar && \  
ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  
  
# get phpunit (http://phpunit.de/)  
RUN curl -Ls -o /usr/local/bin/phpunit.phar
https://phar.phpunit.de/phpunit.phar && \  
chmod 755 /usr/local/bin/phpunit.phar && \  
ln -s /usr/local/bin/phpunit.phar /usr/local/bin/phpunit  
  
ADD php-choose-version /usr/sbin/php-choose-version  
RUN php-choose-version 7.0  
  
# clean  
RUN apt-clean  
# EOF  

