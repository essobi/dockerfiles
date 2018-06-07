FROM ej52/alpine-nginx-php  
  
MAINTAINER David Savell https://github.com/dsavell  
  
# Install Core Packages  
RUN \  
apk add --no-cache curl unzip --virtual=build-dependencies  
  
# Download & Extract GRAV  
WORKDIR /var/www/  
RUN \  
rm -fR /var/www/* \  
&& SKELETON_VERSION=$(curl -sX GET "https://api.github.com/repos/getgrav/grav-
skeleton-blog-site/releases/latest" | awk '/tag_name/{print $4;exit}'
FS='[""]') \  
&& curl -o grav-skeleton-blog-site.zip -L https://github.com/getgrav/grav-
skeleton-blog-site/releases/download/${SKELETON_VERSION}/grav-skeleton-blog-
site-v${SKELETON_VERSION}.zip \  
&& unzip grav-skeleton-blog-site.zip \  
&& cp -R /var/www/grav-skeleton-blog-site/* /var/www  
  
# Install GRAV  
WORKDIR /var/www/  
RUN \  
bin/gpm selfupgrade \  
&& bin/gpm install admin \  
&& bin/gpm update \  
&& chown -R www-data:www-data * \  
&& find . -type f | xargs chmod 664 \  
&& find . -type d | xargs chmod 775 \  
&& find . -type d | xargs chmod +s \  
&& umask 0002  
# Clean  
WORKDIR /var/www/  
RUN \  
rm -rf grav-skeleton-blog-site \  
&& rm -rf grav-skeleton-blog-site.zip \  
&& apk del --purge build-dependencies  
  
# Volume  
VOLUME /var/www  
  
# Exposed Ports  
EXPOSE 80  

