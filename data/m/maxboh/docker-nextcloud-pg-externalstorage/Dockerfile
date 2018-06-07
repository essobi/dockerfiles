FROM quay.io/rootlogin/nextcloud:latest  
MAINTAINER Max Bohnet <github.com/MaxBo>  
  
# install Access Control List acl and set default read and write permissions
for the nextcloud user  
RUN apk add \--update acl \  
&& mkdir /var/local_workspace \  
&& setfacl -m user:nextcloud:rwX /var/local_workspace \  
&& setfacl -d -m user:nextcloud:rwX /var/local_workspace \  
&& setfacl -R -m m:rwx /var/local_workspace \  
&& chmod -R 750 /var/local_workspace  
  
# remove X-Frame-Options from nginx configuration, which is seen as a security
risk  
RUN sed -i '/add_header X-Frame-Options SAMEORIGIN;/d' /etc/nginx/nginx.conf  
  

