FROM debian:8  
MAINTAINER Firdaws Aboulaye <aboufred@gmail.com>  
  
ENV FUSIONDIRECTORY_VERSION=\  
LDAP_DOMAIN=example.com \  
LDAP_PASSWORD=s3cr3tpassw0rd \  
FUSIONDIRECTORY_PASSWORD=s3cr3tpassw0rd \  
SMTP_HOST=smtp \  
SMTP_PORT=25 \  
SMTP_TLSCERTCHECK=off  
  
COPY apache.conf /etc/apache2/sites-available/000-default.conf  
COPY fusiondirectory.conf /  
COPY msmtp.conf /  
COPY docker-entrypoint.sh /  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& export LC_ALL=en_US.UTF-8 \  
&& gpg --keyserver keys.gnupg.net --recv-key 62B4981F \  
&& gpg --export -a "Fusiondirectory Archive Manager
<contact@fusiondirectory.org>" > FD-archive-key \  
&& apt-key add FD-archive-key \  
&& echo "deb http://repos.fusiondirectory.org/debian-jessie jessie main" \  
> etc/apt/sources.list.d/fusiondirectory-jessie.list \  
&& echo "deb http://repos.fusiondirectory.org/debian-extra jessie main" \  
>> etc/apt/sources.list.d/fusiondirectory-jessie.list \  
&& apt-get update \  
&& apt-get install -y php-mdb2 msmtp \  
-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \  
fusiondirectory=${FUSIONDIRECTORY_VERSION:-*} \  
fusiondirectory-plugin-mail=${FUSIONDIRECTORY_VERSION:-*} \  
fusiondirectory-plugin-ldapmanager=${FUSIONDIRECTORY_VERSION:-*} \  
&& chmod +x docker-entrypoint.sh \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80  
ENTRYPOINT ["/docker-entrypoint.sh"]  

