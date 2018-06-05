#  
# php7:dbg Dockerfile  
#  
# https://github.com/rzani/docker-repos  
FROM rzani/php7  
  
# File Author  
MAINTAINER Rodrigo Zani <rodrigo.zhs@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -yq --force-yes php7.0-dbg  
  
# Turn display_errors on  
RUN sed -i "s/display_errors = Off/display_errors = On/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/html_errors = Off/html_errors = On/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/display_errors = Off/display_errors = On/"
/etc/php/7.0/cli/php.ini  
RUN sed -i "s/html_errors = Off/html_errors = On/" /etc/php/7.0/cli/php.ini  
  
# Clean apt-get and other unusual things  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN rm -Rf /var/cache/* && \  
rm -Rf /usr/share/doc/* && \  
rm -Rf /usr/share/man/*  

