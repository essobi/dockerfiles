FROM madehao/centos:6  
MAINTAINER madehao1983@sina.com  
  
# install nesessary software  
RUN yum -y install gcc openssl-devel zlib-devel pcre-devel  
  
# create user  
RUN groupadd nginx -g 5000 \  
&& useradd -d /fs -g nginx -m nginx -u 5000  
  
# get nginx  
WORKDIR /tmp  
  
RUN curl http://nginx.org/download/nginx-1.12.2.tar.gz -O  
  
# install nginx  
RUN tar -zxvf nginx-1.12.2.tar.gz  
  
WORKDIR /tmp/nginx-1.12.2  
RUN ./configure \  
\--prefix=/fs/nginx \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_gzip_static_module \  
\--with-http_gunzip_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_stub_status_module \  
\--user=nginx \  
\--group=nginx \  
&& make \  
&& make install  
  
# remove downloaded file  
WORKDIR /  
RUN rm -fr /tmp/nginx-1.12.2 /tmp/nginx-1.12.2.tar.gz  
  
# other enviroment  
RUN chown -R nginx:nginx /fs/nginx \  
&& chown root /fs/nginx/sbin/nginx \  
&& chmod 4111 /fs/nginx/sbin/nginx \  
&& alternatives --install /usr/local/bin/nginx nginx /fs/nginx/sbin/nginx
11202  
  
USER nginx  
CMD ["nginx"]  
  
ONBUILD USER root  

