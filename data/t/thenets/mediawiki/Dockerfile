FROM mediawiki  
  
# Install updates  
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y && \  
# Mail dependencies  
pear install mail net_smtp && \  
apt-get autoremove -y && apt-get clean && rm -r /var/lib/apt/lists/*  
  
ENV APP_DIR=/var/www/html  
ENV EXTENSIONS="Duplicator Echo MobileFrontend VisualEditor NetworkAuth"  
WORKDIR $APP_DIR/data  
  
# Install extensions  
RUN cd $APP_DIR/extensions && \  
for EXTENSION in $EXTENSIONS; do \  
cd $APP_DIR/extensions && \  
git clone \--depth 1 -b $MEDIAWIKI_BRANCH
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/"$EXTENSION".git && \  
cd $APP_DIR/extensions/$EXTENSION && \  
git submodule update --init ; \  
done && \  
chown -R 1000.1000 $APP_DIR/extensions/  
  
# Move all persistent data to $APP_DIR/data  
# and fallback compatibility with symbolic links  
RUN mkdir -p $APP_DIR/data && \  
# Image dir  
mv $APP_DIR/images/ $APP_DIR/data/images && \  
ln -s $APP_DIR/data/images $APP_DIR/images && \  
# Main config file  
ln -s $APP_DIR/data/LocalSettings.php $APP_DIR/LocalSettings.php  
  
# Enable Apache Modules  
RUN a2enmod rewrite  
  
# .htaccess to volume  
WORKDIR $APP_DIR  
RUN ln -s data/conf_htaccess .htaccess  
  
# Entrypoint  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  
  
VOLUME ["$APP_DIR/data"]  

