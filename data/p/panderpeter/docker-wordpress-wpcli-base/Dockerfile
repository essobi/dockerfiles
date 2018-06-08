# # Installs WordPress with wp-cli (wp.cli.org) installed  
# Docker Hub: https://registry.hub.docker.com/u/conetix/wordpress-with-wp-cli/  
# Github Repo: https://github.com/conetix/docker-wordpress-wp-cli  
  
FROM wordpress  
  
RUN apt-get update &&\  
apt-get install -y git &&\  
apt-get install -y unzip &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/*  
# Load and install plugins  
RUN curl -o /tmp/advanced-custom-fields.zip
https://downloads.wordpress.org/plugin/advanced-custom-fields.4.4.12.zip &&\  
curl -o /tmp/advanced-code-editor.zip
https://downloads.wordpress.org/plugin/advanced-code-editor.2.2.7.zip &&\  
curl -o /tmp/importer.zip https://downloads.wordpress.org/plugin/wordpress-
importer.0.6.3.zip &&\  
curl -o /tmp/wp-scss.zip https://downloads.wordpress.org/plugin/wp-
scss.1.2.2.zip &&\  
curl -o /tmp/wpide.zip https://downloads.wordpress.org/plugin/wpide.2.4.0.zip
&&\  
curl -o /tmp/tinymce.zip https://downloads.wordpress.org/plugin/tinymce-
advanced.4.6.3.zip &&\  
curl -o /tmp/qtranslate-x.zip
https://downloads.wordpress.org/plugin/qtranslate-x.3.4.6.8.zip &&\  
curl -o /tmp/acf-qtranslate.zip https://downloads.wordpress.org/plugin/acf-
qtranslate.1.7.23.zip &&\  
curl -o /tmp/revisr.zip https://downloads.wordpress.org/plugin/revisr.zip  
  
RUN cd /usr/src/wordpress/wp-content/plugins/ &&\  
unzip /tmp/advanced-custom-fields.zip &&\  
unzip /tmp/advanced-code-editor.zip &&\  
unzip /tmp/importer.zip &&\  
unzip /tmp/wp-scss.zip &&\  
unzip /tmp/wpide.zip &&\  
unzip /tmp/tinymce.zip &&\  
unzip /tmp/qtranslate-x.zip &&\  
unzip /tmp/acf-qtranslate.zip &&\  
unzip /tmp/revisr.zip  
  

