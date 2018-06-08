FROM httpd:latest  
  
LABEL maintainer "Monsieur Biz <docker@monsieurbiz.com>"  
  
ARG HTTPD_CONFIG_FILE=/usr/local/apache2/conf/httpd.conf  
RUN \  
# Activate some modules  
modules="proxy_http2_module http2_module rewrite_module ssl_module
deflate_module expires_module proxy_fcgi_module proxy_http_module
proxy_module"; \  
for module in $modules; do \  
sed -i "s/#LoadModule $module/LoadModule $module/" $HTTPD_CONFIG_FILE; \  
done; \  
echo "IncludeOptional sites-enabled/*.conf" >> $HTTPD_CONFIG_FILE;  
  

