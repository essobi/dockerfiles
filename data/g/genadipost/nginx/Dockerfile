FROM centos/httpd-24-centos7  
  
ENV SUMMARY="Nginx Documentation" \  
DESCRIPTION="Nginx Documentation as it seen in http://nginx.org/ and
https://docs.nginx.com. \  
The image is based on centos/httpd-24-centos7 to run unprivileged httpd
container."  
  
LABEL summary="$SUMMARY" \  
description="$DESCRIPTION" \  
io.k8s.description="$DESCRIPTION" \  
io.k8s.display-name="Nginx Documentation" \  
io.openshift.expose-services="8080:http,8443:https" \  
io.openshift.tags="documentation,docs,nginx" \  
name="dockerized-docs/nginx" \  
maintainer="Ron Cohen <roncohen04@gmail.com>, Genadi Postrilko
<genadipost@gmail.com>"  
  
user root  
  
# Install httrack to get docs  
RUN yum -y install httrack  
  
USER default  
  
# Get the nginx docs sites  
RUN mkdir -p /opt/app-root/src/nginx-docs/docs-nginx-com \  
&& cd /opt/app-root/src/nginx-docs && httrack https://nginx.org/ \  
&& cd /opt/app-root/src/nginx-docs/docs-nginx-com && httrack
https://docs.nginx.com  
  
# Set httpd to nginx-docs  
RUN rm -rf /var/www/html && \  
ln -s /opt/app-root/src/nginx-docs /var/www/html && \  
mv /var/www/html/docs-nginx-com/docs.nginx.com/ /var/www/html/docs.nginx.com/  
  
# Connect between sites com/docs and org  
RUN cat /var/www/html/nginx.org/en/docs/index.html \  
| awk '{gsub(/"https\:\/\/www\\.nginx\\.com\/resources\/admin-guide\/"/,
"\"/docs.nginx.com/nginx/admin-guide/\"")}1' > /var/www/html/tmp.html && \  
rm -rf /var/www/html/nginx.org/en/docs/index.html && cp /var/www/html/tmp.html
/var/www/html/nginx.org/en/docs/index.html && \  
echo "RedirectMatch ^/$ /nginx.org/en/docs/index.html" >>
/etc/httpd/conf/httpd.conf  
  
CMD ["/usr/bin/run-httpd"]  

