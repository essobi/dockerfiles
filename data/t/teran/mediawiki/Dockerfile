FROM teran/php7-fpm:latest  
  
MAINTAINER Igor Shishkin <me@teran.ru>  
  
ARG major=1.31  
ARG minor=0-rc.2  
LABEL application=mediawiki  
LABEL version=${major}.${minor}  
LABEL description="Mediawiki==${major}.${minor} with nginx and php7-fpm"  
  
RUN wget -O- https://www.mediawiki.org/keys/keys.txt | gpg --import  
  
RUN wget -O /tmp/mediawiki.tgz
https://releases.wikimedia.org/mediawiki/${major}/mediawiki-${major}.${minor}.tar.gz
&& \  
wget -O /tmp/mediawiki.sig
https://releases.wikimedia.org/mediawiki/${major}/mediawiki-${major}.${minor}.tar.gz.sig
&& \  
gpg --verify /tmp/mediawiki.sig /tmp/mediawiki.tgz && \  
mkdir -p /var/www && \  
tar xzf /tmp/mediawiki.tgz -C /tmp && \  
cp -r /tmp/mediawiki*/* /var/www/ && \  
rm -rf /tmp/mediawiki*  
ADD nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80  

