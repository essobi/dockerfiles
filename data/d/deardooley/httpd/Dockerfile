######################################################  
#  
# Apache 2.4 Base Image  
# Tag: deardooley/apache:alpine  
#  
# Minimal Apache 2.4 image with CORS, rewrite, and proxy  
# support. Default unified logging to standard out.  
#  
######################################################  
  
FROM gliderlabs/alpine:3.4  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu  
  
ADD tcp/limits.conf /etc/security/limits.conf  
ADD tcp/sysctl.conf /etc/sysctl.conf  
  
RUN apk --update add openssl apache2 vim gzip tzdata bash && \  
apk --update add apache2-ssl && \  
rm -f /var/cache/apk/* && \  
  
# Set up system timezone and sync  
echo "Setting system timezone to America/Chicago..." && \  
ln -snf /usr/share/zoneinfo/America/Chicago /etc/localtime && \  
#echo $(setup-ntp -c busybox 2>&1) && \  
ntpd -d -p pool.ntp.org && \  
  
echo "Updating default apache DocumentRoot..." && \  
mv /var/www/localhost/htdocs /var/www/html && \  
# addgroup -S apache && \  
chown -R apache:apache /var/www/html && \  
sed -i 's#/var/www/localhost/htdocs#%DOCUMENT_ROOT%#g' /etc/apache2/httpd.conf
&& \  
sed -i 's/^ AllowOverride None/ AllowOverride All/' /etc/apache2/httpd.conf &&
\  
#sed -i 's#LogLevel warn#LogLevel info#g' /etc/apache2/httpd.conf && \  
sed -i 's#logs/error.log#/proc/self/fd/2#g' /etc/apache2/httpd.conf && \  
sed -i 's#logs/access.log#/proc/self/fd/1#g' /etc/apache2/httpd.conf && \  
  
# update default server hostname to a template variable we can replace at
runtime  
sed -i 's/^#ServerName .*/ServerName %HOSTNAME%:80/g' /etc/apache2/httpd.conf
&& \  
sed -i 's/^ServerName .*/ServerName %HOSTNAME%:443/g'
/etc/apache2/conf.d/ssl.conf && \  
  
# update document root to a template variable we can replace at runtime.  
sed -i 's#/var/www/localhost/htdocs#%DOCUMENT_ROOT%#g'
/etc/apache2/conf.d/ssl.conf && \  
  
# update logging levels  
sed -i 's#^SSLMutex .*#Mutex sysvsem default#g' /etc/apache2/conf.d/ssl.conf
&& \  
sed -i 's#logs/ssl_error.log#/proc/self/fd/2#g' /etc/apache2/conf.d/ssl.conf
&& \  
sed -i 's#logs/ssl_access.log#/proc/self/fd/1#g' /etc/apache2/conf.d/ssl.conf
&& \  
sed -i 's#logs/ssl_request.log#/proc/self/fd/1#g' /etc/apache2/conf.d/ssl.conf
&& \  
#sed -i 's#LogLevel warn#LogLevel info#g' /etc/apache2/conf.d/ssl.conf && \  
mkdir /etc/apache2/run && \  
sed -i 's#/run/apache2#/etc/apache2/run#g' /etc/apache2/httpd.conf && \  
sed -i 's#/run/apache2#/etc/apache2/run#g' /etc/apache2/conf.d/ssl.conf && \  
rm -f /etc/apache2/conf.d/mpm.conf && \  
rm -f /etc/apache2/conf.d/info && \  
rm -f /etc/apache2/conf.d/userdir.conf && \  
sed -i 's/^#LoadModule rewrite_module/LoadModule rewrite_module/'
/etc/apache2/httpd.conf && \  
sed -i 's/^#LoadModule deflate_module/LoadModule deflate_module/g'
/etc/apache2/httpd.conf && \  
sed -i 's/^#LoadModule expires_module/LoadModule expires_module/g'
/etc/apache2/httpd.conf && \  
  
echo 'PidFile "/etc/apache2/run/httpd.pid"' >> /etc/apache2/httpd.conf  
  
  
#  
# RUN apk --update add apache2-proxy apache2-proxy-html vim gzip tzdata bash
curl && \  
# rm -f /var/cache/apk/* && \  
# /usr/sbin/deluser apache && \  
#  
# addgroup -g 50 -S apache && \  
# adduser -u 1000 -g apache -G apache -S apache && \  
# mkdir /run/apache2 && \  
# chown -R apache:root /run/apache2 && \  
#  
# # Set up system timezone and sync  
# echo "Setting system timezone to America/Chicago..." && \  
# ln -snf /usr/share/zoneinfo/America/Chicago /etc/localtime && \  
# ntpd -d -p pool.ntp.org && \  
#  
# echo "Updating default apache DocumentRoot..." && \  
# mkdir /var/www/html && \  
# chown -R apache:apache /var/www/html && \  
# # fix bug in proxy.conf and proxy-html.conf in stock apache install  
# sed -i 's/^ AllowOverride None/ AllowOverride All/' /etc/apache2/httpd.conf
&& \  
# sed -i 's/^#LoadModule slotmem_shm_module/LoadModule slotmem_shm_module/'
/etc/apache2/httpd.conf && \  
# sed -i 's/^#LoadModule socache_shmcb_module/LoadModule
socache_shmcb_module/' /etc/apache2/httpd.conf && \  
# sed -i 's/^#LoadModule rewrite_module/LoadModule rewrite_module/'
/etc/apache2/httpd.conf && \  
# sed -i 's#/usr/lib/libxml2.so$#/usr/lib/libxml2.so.2#'
/etc/apache2/conf.d/proxy-html.conf && \  
# sed -i 's#/usr/lib/libxml2.so$#/usr/lib/libxml2.so.2#'
/etc/apache2/conf.d/proxy.conf && \  
# sed -i 's#/var/www/localhost/htdocs#%DOCUMENT_ROOT%#g'
/etc/apache2/httpd.conf && \  
# # sed -i 's#^SSLMutex .*#Mutex sysvsem default#g'
/etc/apache2/conf.d/ssl.conf && \  
#  
# # update logging to write  
# sed -i 's#/var/www/localhost/htdocs#%DOCUMENT_ROOT%#g'
/etc/apache2/httpd.conf && \  
# #sed -i 's#LogLevel warn#LogLevel info#g' /etc/apache2/httpd.conf && \  
# sed -i 's#^ErrorLog logs/error.log#ErrorLog /proc/self/fd/2#g'
/etc/apache2/httpd.conf && \  
# sed -i 's#^CustomLog logs/access.log combined#CustomLog /proc/self/fd/1
combined#g' /etc/apache2/httpd.conf  
# # sed -i 's#^SSLMutex .*#Mutex sysvsem default#g'
/etc/apache2/conf.d/ssl.conf && \  
# # sed -i 's#^ErrorLog logs/ssl_error.log#ErrorLog /proc/self/fd/2#g'
/etc/apache2/conf.d/ssl.conf && \  
# # sed -i 's#^TransferLog logs/ssl_access.log#TransferLog /proc/self/fd/1#g'
/etc/apache2/conf.d/ssl.conf && \  
# # sed -i 's#^CustomLog logs/ssl_request.log#CustomLog /proc/self/fd/1#g'
/etc/apache2/conf.d/ssl.conf && \  
# #sed -i 's#LogLevel warn#LogLevel info#g' /etc/apache2/conf.d/ssl.conf && \  
#  
# # sed -i 's#^SSLProtocol .*#SSLProtocol all -SSLv2 -SSLv3#g'
/etc/apache2/conf.d/ssl.conf  
  
ADD docker_entrypoint.sh /docker_entrypoint.sh  
  
WORKDIR /var/www/html  
  
EXPOSE 80 443  
  
ENTRYPOINT ["/docker_entrypoint.sh"]  
  
CMD ["httpd", "-DFOREGROUND"]  

