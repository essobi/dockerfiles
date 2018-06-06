FROM thenextapps/base-nginxphp:v1  
MAINTAINER thenextapps@gmail.com  
  
RUN \  
cd /srv/www/public && \  
wget https://s3-ap-southeast-2.amazonaws.com/lmc-libs/chatstack-
build-v5.4.4568.release.zip && \  
unzip chatstack-build-v5.4.4568.release.zip && \  
rm -rf chatstack-build-v5.4.4568.release.zip && \  
chmod 777 /srv/www/public/livehelp/include/database.php  
  
WORKDIR /srv/www/public  
  
CMD /tmp/start-server.sh && /sbin/my_init && sudo service postfix start  
  
EXPOSE 8089 8090 8091

