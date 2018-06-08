FROM vguardiola/gentoo  
MAINTAINER Victor Guardiola <victor@masquesoft.net>  
RUN echo "PHP_INI_VERSION=\"production\"" >> /etc/portage/make.conf  
RUN echo "PHP_TARGETS=\"php5-6\"" >> /etc/portage/make.conf  
COPY ./etc/locale.nopurge /etc/locale.nopurge  
COPY ./etc/portage/package.keywords/php /etc/portage/package.keywords/php  
COPY ./etc/portage/package.use/imagemagick
/etc/portage/package.use/imagemagick  
COPY ./etc/portage/package.use/php /etc/portage/package.use/php  
RUN FEATURES="-sandbox -usersandbox" emerge -1 -j1 dev-libs/gobject-
introspection  
RUN emerge -D dev-lang/php app-eselect/eselect-php dev-php/pecl-redis \  
=dev-php/pecl-apcu-4.0.10 dev-php/pecl-imagick dev-php/pecl-timezonedb \  
dev-vcs/git app-admin/supervisor && eclean-dist -dqf && localepurge && rm
/usr/portage/distfiles -rf  
EXPOSE 9000  
CMD ["php-fpm", "-c", "/etc/php/fpm-php5.6/php.ini", "-y", "/etc/php/fpm-
php5.6/php-fpm.conf", "-F"]  

