FROM nlesc/xenon-alpine-base  
MAINTAINER Stefan Verhoeven "s.verhoeven@esciencecenter.nl"  
RUN apk add --no-cache apache2-webdav apache2-utils curl && \  
htpasswd -bc /var/www/users.htpasswd xenon javagat && \  
mkdir /run/apache2 && \  
  
# make directory for DavLockDB (see ./httpd.conf)  
mkdir /var/www/var && \  
chown apache.apache /var/www/var && \  
  
# make xenon user writable directory  
mkdir /home/xenon/uploads && \  
chown apache.apache /home/xenon/uploads && \  
  
# Xenon's filesystem integration tests expect certain directory structure,
create it here:  
# make directory that user xenon can write in  
mkdir /var/www/uploads && \  
cd /var/www/uploads && \  
mkdir -p filesystem-test-fixture/links && \  
echo "Hello World" > filesystem-test-fixture/links/file0 && \  
touch filesystem-test-fixture/links/file1 && \  
ln -s /var/www/uploads/filesystem-test-fixture/links/file0
/var/www/uploads/filesystem-test-fixture/links/link0 && \  
ln -s /var/www/uploads/filesystem-test-fixture/links/file1
/var/www/uploads/filesystem-test-fixture/links/link1 && \  
ln -s /var/www/uploads/filesystem-test-fixture/links/file2
/var/www/uploads/filesystem-test-fixture/links/link2 && \  
ln -s /var/www/uploads/filesystem-test-fixture/links/link0
/var/www/uploads/filesystem-test-fixture/links/link3 && \  
ln -s /var/www/uploads/filesystem-test-fixture/links/link2
/var/www/uploads/filesystem-test-fixture/links/link4 && \  
ln -s /var/www/uploads/filesystem-test-fixture/links/link6
/var/www/uploads/filesystem-test-fixture/links/link5 && \  
ln -s /var/www/uploads/filesystem-test-fixture/links/link5
/var/www/uploads/filesystem-test-fixture/links/link6 && \  
chown -R apache.apache /var/www/uploads && \  
cd /home/xenon && \  
  
# Xenon's filesystem integration tests expect certain directory structure,
create it here:  
# make directory that anonymous user can write in  
mkdir /var/www/localhost/htdocs/downloads && \  
cd /var/www/localhost/htdocs/downloads && \  
mkdir -p filesystem-test-fixture/links && \  
echo "Hello World" > filesystem-test-fixture/links/file0 && \  
touch filesystem-test-fixture/links/file1 && \  
ln -s /var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/file0
/var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link0 && \  
ln -s /var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/file1
/var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link1 && \  
ln -s /var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/file2
/var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link2 && \  
ln -s /var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link0
/var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link3 && \  
ln -s /var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link2
/var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link4 && \  
ln -s /var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link6
/var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link5 && \  
ln -s /var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link5
/var/www/localhost/htdocs/downloads/filesystem-test-fixture/links/link6 && \  
chown -R apache.apache /var/www/localhost/htdocs/downloads/filesystem-test-
fixture && \  
cd /home/xenon  
  
ADD httpd.conf /etc/apache2/httpd.conf  
  
EXPOSE 80  
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]  
  
HEALTHCHECK --interval=1s CMD curl -f http://localhost/ || exit 1  

