FROM monsieurbiz/httpd:latest  
  
ARG HTTPD_CONFIG_FILE=/usr/local/apache2/conf/httpd.conf  
RUN sed -i "s/#LoadModule macro_module/LoadModule macro_module/"
$HTTPD_CONFIG_FILE;  
  
# Use www-data with correct UID  
ARG USER_UID=501  
RUN usermod -u $USER_UID www-data

