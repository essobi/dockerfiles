FROM httpd:2.4.29  
MAINTAINER Ryu Sato <ryu@weseek.co.jp>  
  
# Const environment  
ARG HTTPD_CONF_PATH="/usr/local/apache2/conf/httpd.conf"  
ARG HTTPD_DOCS_PATH="/usr/local/apache2/htdocs"  
ARG HTTPD_EXTRA_CONF_DIR="/usr/local/apache2/conf/extra"  
# Install initial contents  
COPY htdocs/ $HTTPD_DOCS_PATH/  
  
# Add extra config  
ARG CONF_PROXY="extra/proxy.conf"  
VOLUME /usr/local/apache2/conf  
VOLUME /usr/local/apache2/htdocs  
  
COPY $CONF_PROXY $HTTPD_EXTRA_CONF_DIR/  
RUN echo "Include conf/$CONF_PROXY" >> $HTTPD_CONF_PATH  

