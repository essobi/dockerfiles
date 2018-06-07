FROM wordpress  
  
#--------------------------  
# Install wordpress plugins  
#--------------------------  
# これから使う`wget`と`unzip`を入れる  
RUN apt-get update  
RUN apt-get -y --force-yes -o Dpkg::Options::="--force-confdef" install wget
unzip  
  
# プラグインファイルの一時ダウンロード先  
WORKDIR /tmp/wp-plugins  
  
# プラグインファイルをダウンロード  
RUN wget https://downloads.wordpress.org/plugin/akismet.4.0.7.zip  
RUN wget https://downloads.wordpress.org/plugin/bbpress.2.5.14.zip  
RUN wget https://downloads.wordpress.org/plugin/ewww-image-optimizer.4.2.1.zip  
RUN wget https://downloads.wordpress.org/plugin/google-sitemap-
generator.4.0.9.zip  
RUN wget https://downloads.wordpress.org/plugin/jetpack.6.2.zip  
RUN wget https://downloads.wordpress.org/plugin/simple-feature-requests.zip  
RUN wget https://downloads.wordpress.org/plugin/pubsubhubbub.2.2.2.zip  
RUN wget https://downloads.wordpress.org/plugin/wordfence.7.1.7.zip  
RUN wget https://downloads.wordpress.org/plugin/wp-fastest-cache.0.8.8.1.zip  
RUN wget https://downloads.wordpress.org/plugin/wp-multibyte-patch.2.8.1.zip  
RUN wget https://downloads.wordpress.org/plugin/wp-azure-offload.1.0.zip  
RUN wget https://downloads.wordpress.org/plugin/wp-mail-smtp.zip  
RUN wget https://downloads.wordpress.org/plugin/wordpress-social-login.zip  
RUN wget https://downloads.wordpress.org/plugin/pixabay-images.zip  
  
# プラグインをWordPressのプラグインディレクトリに解凍する  
RUN unzip -o './*.zip' -d /usr/src/wordpress/wp-content/plugins  
RUN chown -R www-data:www-data /usr/src/wordpress/wp-content  
  
# 一時ダウンロード先内の全ファイルの削除  
RUN rm -rf '/tmp/wp-plugins'  
  
# 戻る  
WORKDIR /var/www/html  
  
#------------------------  
# Install Wordpress theme  
#------------------------  
# テーマファイルの一時ダウンロード先  
WORKDIR /tmp/wp-themes  
  
ENV cocoonversion=0.6.3.2  
# テーマファイルをダウンロード  
RUN wget https://github.com/ebibibi/appservice-
wordpress/raw/master/Themes/cocoon-child-master.zip  
RUN wget https://github.com/yhira/cocoon/archive/${cocoonversion}.zip  
  
# テーマをWordPressのテーマディレクトリに解凍する  
RUN unzip './*.zip' -d /usr/src/wordpress/wp-content/themes  
RUN mv /usr/src/wordpress/wp-content/themes/cocoon-${cocoonversion}
/usr/src/wordpress/wp-content/themes/cocoon-master  
RUN chown -R www-data:www-data /usr/src/wordpress/wp-content  
  
# 一時ダウンロード先内の全ファイルの削除  
RUN rm -rf '/tmp/wp-themes'  
  
# 戻る  
WORKDIR /var/www/html  
  
#------------------------  
# 実行  
#------------------------  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]

