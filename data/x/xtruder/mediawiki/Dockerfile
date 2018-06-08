FROM php:5.6-apache  
MAINTAINER Jaka Hudoklin <jaka@x-truder.net>  
  
ARG MEDIAWIKI_VERSION=wmf/1.31.0-wmf.11  
WORKDIR /var/www/html  
  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
g++ \  
libicu52 \  
libicu-dev \  
libzip-dev \  
imagemagick \  
libldb-dev \  
libaprutil1-dev \  
git \  
&& ln -fs /usr/lib/x86_64-linux-gnu/libzip.so /usr/lib/ \  
&& ln -fs /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/ \  
&& docker-php-ext-install intl mysqli zip mbstring opcache fileinfo \  
&& apt-get purge -y --auto-remove g++ libicu-dev libzip-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod rewrite  
  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
RUN set -x; \  
git clone \--depth 1 -b ${MEDIAWIKI_VERSION}
https://github.com/wikimedia/mediawiki.git . && \  
git clone \--depth 1 https://github.com/wikimedia/mediawiki-extensions.git
external_extensions  
  
COPY php.ini /usr/local/etc/php/conf.d/mediawiki.ini  
  
COPY apache/mediawiki.conf /etc/apache2/  
RUN echo "Include /etc/apache2/mediawiki.conf" >> /etc/apache2/apache2.conf  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  
  
ARG
MEDIAWIKI_SKINS=CologneBlue,Modern,MonoBook,Nostalgia,Vector,MinervaNeue,Timeless  
  
RUN set -x; \  
for name in $(echo $MEDIAWIKI_SKINS | sed "s/,/ /g"); do \  
git submodule update --init --recursive skins/$name; \  
done  
  
ARG
MEDIAWIKI_EXTENSIONS=CirrusSearch,Cite,CiteThisPage,CodeEditor,Elastica,Gadgets,ImageMap,InputBox,Interwiki,LocalisationUpdate,MobileFrontend,Nuke,ParserFunctions,PdfHandler,Popups,Renameuser,Scribunto,SyntaxHighlight_GeSHi,TitleBlacklist,VisualEditor,WikiEditor,Wikibase,Math,RelatedArticles,ArticlePlaceholder,PropertySuggester  
  
RUN set -x; \  
for name in $(echo $MEDIAWIKI_EXTENSIONS | sed "s/,/ /g"); do \  
git submodule update --init --recursive extensions/$name; \  
done  
  
ARG MEDIAWIKI_EXTERNAL_EXTENSIONS=NetworkAuth,LinkedWiki,ReplaceText  
  
RUN set -x; \  
cd external_extensions && \  
for name in $(echo $MEDIAWIKI_EXTERNAL_EXTENSIONS | sed "s/,/ /g"); do \  
git submodule update --init --recursive $name && \  
ln -fs -t ../extensions $PWD/$name; \  
done  
  
COPY composer.local.json composer.local.json  
RUN composer update --no-dev  
RUN cd extensions/Wikibase && composer install --no-dev  
RUN cd extensions/Elastica && composer install --no-dev  

