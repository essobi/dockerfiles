FROM wordpress:4-fpm  
  
RUN \  
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
RUN \  
echo 'alias wp="wp --allow-root"' >> $HOME/.bashrc  

