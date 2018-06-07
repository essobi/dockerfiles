FROM php:7.0-apache  
ENV TYPECHO_MAJOR_VER 1.0  
ENV TYPECHO_VER 14.10.10  
ADD entrypoint.sh /entrypoint.sh  
RUN apt-get update && apt-get install -y unzip \  
&& cd /tmp && curl -o typecho.tar.gz -L
https://github.com/typecho/typecho/releases/download/v$TYPECHO_MAJOR_VER-$TYPECHO_VER-
release/$TYPECHO_MAJOR_VER.$TYPECHO_VER.-release.tar.gz \  
&& tar -xvf typecho.tar.gz && mv -f /tmp/build/* /var/www/html/ \  
&& curl -o typecho_material_theme.zip -L
https://github.com/Hanccc/typecho_material_theme/archive/master.zip \  
&& unzip typecho_material_theme.zip && mv ./typecho_material_theme-master
/var/www/html/usr/themes/typecho_material_theme \  
&& curl -o typecho_lanyon_theme.zip -L https://github.com/LjxPrime/lanyon-
typecho/archive/master.zip \  
&& unzip typecho_lanyon_theme.zip && mv ./lanyon-typecho-master
/var/www/html/usr/themes/lanyon-typecho \  
&& chmod -R 777 /var/www/html && chmod +x /entrypoint.sh \  
&& rm -rf /tmp/* \  
&& apt-get purge -y --auto-remove unzip  
VOLUME /data  
  
ENTRYPOINT ["/entrypoint.sh"]

