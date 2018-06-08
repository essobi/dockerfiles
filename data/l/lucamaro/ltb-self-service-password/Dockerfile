FROM php:7-apache  
MAINTAINER Luca Maragnani "luca.maragnani@gmail.com"  
# Installation of nesesary package/software for this containers...  
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && apt-get upgrade
-y \  
&& apt-get install -y -q --no-install-recommends \  
libldap2-dev \  
libmcrypt-dev \  
wget \  
# See https://serverfault.com/questions/633394/php-configure-not-finding-ldap-
header-libraries  
&& ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \  
&& ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so \  
&& docker-php-ext-install ldap mcrypt mbstring \  
&& cd /var/www && rm -rf html \  
&& wget -q -O - http://ltb-project.org/archives/ltb-project-self-service-
password-1.0.tar.gz | tar xzf - \  
&& mv ltb-project-self-service-password-1.0 html \  
&& apt-get remove --auto-remove -y gcc m4 dpkg-dev libc6-dev libgcc-4.9-dev \  
libpcre3-dev linux-libc-dev \  
&& apt-get remove -y libldap2-dev libmcrypt-dev \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/src/* \  
# workaround for issue #128 about reset token  
echo "output_buffering = On" > /usr/local/etc/php/php.ini  
  
EXPOSE 80  
  
# init script as entrypoint for initial configuration  
COPY entrypoint.sh /usr/local/bin  
ENTRYPOINT ["sh", "/usr/local/bin/entrypoint.sh", "-DFOREGROUND"]  
  
  
  

