FROM nginx:latest  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/var/www/app","/var/run"]  
EXPOSE 80 443 25 587  
RUN apt-get update && \  
apt-get install nfs-common -y && \  
mkdir /var/www/html && \  
mkdir /lamsa-efs && \  
mkdir /tmp/s3-cache-data && \  
mkdir /tmp/s3-cache && \  
mkdir /s3fs-fuse  
  
RUN apt-get install build-essential git libfuse-dev libcurl4-openssl-dev
libxml2-dev mime-support automake libtool -y  
RUN apt-get install pkg-config libssl-dev -y  
RUN apt-get install git -y  
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse  
RUN cd /s3fs-fuse && ./autogen.sh && ./configure --prefix=/usr --with-openssl
&& make && make install  
  
#USER root  
#CMD ["nginx", "-g daemon off;"]  
CMD mount -t nfs4 -o
nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 ${EFS_URL}:/
/lamsa-efs && \  
mount --bind \--verbose /lamsa-efs/joomla/lamsa_content_managment_testing
/var/www/app/web && \  
s3fs lamsa-content-testing /var/www/app/web/plugins/system/xcrud/xcrud/upload
-o
passwd_file=/var/www/app/web/plugins/system/xcrud/xcrud/aws/passwd,uid=1000,gid=1000,allow_other,use_cache=/tmp/s3-cache-
data/,default_acl=public-read,use_cache=/tmp/s3-cache/ && \  
/usr/sbin/nginx -g 'daemon off;'

