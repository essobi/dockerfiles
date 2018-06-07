FROM grossws/centos:7  
MAINTAINER Konstantin Gribov <grossws@gmail.com>  
  
RUN rpm --import https://nginx.org/keys/nginx_signing.key \  
&& echo -e "[nginx]\nname=nginx
repo\nbaseurl=http://nginx.org/packages/mainline/centos/7/\$basearch/\ngpgcheck=1\nenabled=1\n"
> /etc/yum.repos.d/nginx.repo \  
&& yum -y install nginx \  
&& yum clean all \  
&& rm /etc/nginx/conf.d/default.conf  
  
CMD ["nginx", "-g", "daemon off;"]  
  

