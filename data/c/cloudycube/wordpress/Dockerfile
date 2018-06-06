FROM cloudycube/nginx-php7  
MAINTAINER Sascha Falk <sascha@falk-online.eu>  
  
# Copy prepared files into the image  
COPY target /  
  
# download ans install the latest wordpress 4.x version  
RUN /bin/bash -c \  
' \  
WP_DEST_PATH="/var/www/html" && \  
WP_REPO_URL="https://github.com/WordPress/WordPress.git" && \  
RELEASE_VERSION_REGEX="[0-9]\\{1,\\}\\.[0-9]\\{1,\\}\\.[0-9]\\{1,\\}" && \  
WP_BRANCH=`git ls-remote --tags $WP_REPO_URL | grep -o "refs/tags/.*" | grep
-o "$RELEASE_VERSION_REGEX" | sort -Vr | head -n1` && \  
echo "Downloading WordPress (version: $WP_BRANCH)" && \  
git clone --single-branch --branch $WP_BRANCH $WP_REPO_URL $WP_DEST_PATH && \  
rm -r $WP_DEST_PATH/.git && \  
chown -R www-data:www-data $WP_DEST_PATH \  
'  
  
# keep the wordpress installation in a volume, so installed plugins survive
container restarts  
VOLUME [ "/var/www/html" ]  

