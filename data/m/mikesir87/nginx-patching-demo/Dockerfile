FROM debian:jessie  
  
WORKDIR /src  
  
RUN apt-get update && \  
apt-get install -y curl make gcc libpcre3-dev zlib1g-dev && \  
# install openssl  
curl -Lo openssl.tar.gz
https://github.com/openssl/openssl/archive/OpenSSL_1_0_1f.tar.gz && \  
tar zxf openssl.tar.gz && \  
mv openssl-* openssl && \  
cd openssl && \  
./config --prefix=/usr/local && \  
make && \  
make install && \  
# build nginx  
curl -Lo nginx.tar.gz http://nginx.org/download/nginx-1.13.5.tar.gz && \  
tar zxf nginx.tar.gz && \  
cd nginx-* && \  
./configure --with-http_ssl_module && \  
make && \  
make install && \  
# cleanup  
rm -rf /src && \  
apt-get autoremove --purge -y curl make gcc && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/local/nginx/html  
  
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout
/usr/local/nginx/conf/cert.key -out /usr/local/nginx/conf/cert.pem -subj
'/CN=localhost/C=US'  
COPY nginx.conf /usr/local/nginx/conf/nginx.conf  
  
CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]  

