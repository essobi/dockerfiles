FROM alpine:latest  
  
# Install apache and link access and error logs to stdout  
RUN apk add \--no-cache apache2-proxy && \  
rm -rf /tmp/* && \  
mkdir /run/apache2 && chown -R apache:apache /run/apache2 && \  
ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log && \  
cat >/etc/apache2/conf.d/proxy.conf  
  
ADD httpd.conf.template /etc/apache2/httpd.conf.template  
  
EXPOSE 80  
  
ENV DOCUMENT_ROOT=/project/www  
  
CMD sed 's/\${DOCUMENT_ROOT}/'"$(echo "$DOCUMENT_ROOT" | sed
's/\//\\\\\//g')"'/g' /etc/apache2/httpd.conf.template >
/etc/apache2/httpd.conf && httpd -DFOREGROUND

