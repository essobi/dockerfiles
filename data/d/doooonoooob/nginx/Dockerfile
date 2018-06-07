FROM doooonoooob/centos  
MAINTAINER doooonooob “doooonoooob@gmai.com"  
#安装依赖包  
RUN yum -y install pcre-devel zlib-devel unzip gcc make  
  
#下载openssl、nginx-ct、nginx  
RUN cd ~ \  
&& curl -O -L https://github.com/openssl/openssl/archive/OpenSSL_1_0_2g.zip \  
&& unzip OpenSSL_1_0_2g.zip \  
&& curl -L -o nginx-ct.zip https://github.com/grahamedgecombe/nginx-
ct/archive/v1.2.0.zip \  
&& unzip nginx-ct.zip \  
&& curl -O http://nginx.org/download/nginx-1.9.14.tar.gz \  
&& tar zxf nginx-1.9.14.tar.gz \  
&& cd nginx-1.9.14 \  
&& ./configure --add-module=../nginx-ct-1.2.0 --with-openssl=../openssl-
OpenSSL_1_0_2g --with-http_v2_module --with-http_ssl_module  
#删除一些不需的文件  
RUN yum clean all \  
&& rm -R ~/*  
  
EXPOSE 80 443  
CMD ["/usr/local/nginx/sbin/nginx"]

