FROM centos:latest  
MAINTAINER ilian  
RUN yum -y update && yum clean all  
RUN yum -y install wget tar perl perl-devel readline-devel pcre-devel openssl-
devel gcc make  
RUN yum -y install GeoIP-devel  
RUN groupadd nginx && useradd -g nginx nginx  
WORKDIR /usr/local/src  
RUN wget https://openresty.org/download/ngx_openresty-1.9.3.1.tar.gz && tar
vxzf ngx_openresty-1.9.3.1.tar.gz  
WORKDIR /usr/local/src/ngx_openresty-1.9.3.1  
RUN ./configure --prefix=/usr/local/openresty --with-pcre-jit --with-ipv6
--with-lua51 --with-http_geoip_module && gmake && gmake install  
WORKDIR /usr/local/openresty/nginx  
#COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf  
RUN mkdir lua  
VOLUME ['conf/', 'logs/', 'lua/']  
EXPOSE 80  
CMD ["sbin/nginx", "-g", "daemon off;"]  

