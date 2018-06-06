FROM alpine  
  
RUN apk --update --no-cache add apache2 && \  
mkdir -p /run/apache2 && chmod 775 /run/apache2 && mkdir -p /web && chown -R
apache:apache /web && \  
sed -i 's/Listen 80/Listen 8080/' /etc/apache2/httpd.conf && \  
sed -i 's#^DocumentRoot ".*#DocumentRoot "/web"#g' /etc/apache2/httpd.conf &&
\  
sed -i 's#^<Directory ".*htdocs.*#<Directory "/web">#' /etc/apache2/httpd.conf
&& \  
sed -i 's/AllowOverride [Nn]one/AllowOverride All/' /etc/apache2/httpd.conf &&
\  
sed -i 's/Require all denied/Require all granted/' /etc/apache2/httpd.conf &&
\  
sed -i 's#logs/.*\\.log#/dev/stdout#g' /etc/apache2/httpd.conf && \  
echo 'Alias "${WEB_PATH}" /web' >> /etc/apache2/httpd.conf && \  
echo "Success."  
  
EXPOSE 8080  
WORKDIR /web  
CMD ["httpd", "-D", "FOREGROUND"]  

