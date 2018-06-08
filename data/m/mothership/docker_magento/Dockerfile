FROM prooph/php:7.0-fpm-xdebug  
  
ENV TERM=xterm  
  
###############################  
# Stuff for terminal #  
###############################  
RUN apk update && apk add --no-cache wget bash ncurses coreutils util-linux
coreutils binutils findutils grep  
  
###############################  
# z.sh #  
###############################  
RUN wget --no-check-certificate https://raw.github.com/rupa/z/master/z.sh -O
/usr/local/bin/z.sh && \  
chmod +x /usr/local/bin/z.sh && \  
echo '. /usr/local/bin/z.sh' >> /root/.bashrc  
  
###############################  
# modman.phar #  
###############################  
RUN curl -sL
https://raw.githubusercontent.com/colinmollenhour/modman/master/modman -o
/usr/local/bin/modman \  
&& chmod +x /usr/local/bin/modman  
  
###############################  
# ceodecept.phar #  
###############################  
RUN curl -sL http://codeception.com/codecept.phar -o /usr/local/bin/codecept \  
&& chmod +x /usr/local/bin/codecept  
  
# magerun.phar #  
###############################  
RUN curl -sL https://files.magerun.net/n98-magerun.phar -o
/usr/local/bin/magerun \  
&& chmod +x /usr/local/bin/magerun  
  
###############################  
# composer.phar #  
###############################  
RUN curl -sL https://getcomposer.org/download/1.2.0/composer.phar -o
/usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer  
  
# Speed up install composer libraries  
RUN composer global require "hirak/prestissimo:^0.3"  
  
  
#ADD ./conf.d/mothership.ini /usr/local/etc/php/conf.d/mothership.ini  
ADD ./conf.d/sendmail.ini /usr/local/etc/php/conf.d/sendmail.ini  
ADD ./etc/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
  
  
#RUN apk del .build-deps && \  
# rm -rf /tmp/*  
  
WORKDIR /var/www/share/dev/

