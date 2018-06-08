FROM library/debian:jessie  
  
ENV OPENRESTY_VERSION 1.7.7.2  
ENV FULLNAME ngx_openresty-$OPENRESTY_VERSION  
ENV FILENAME $FULLNAME.tar.gz  
  
RUN apt-get update && \  
apt-get -y install \  
curl \  
gcc \  
libreadline-dev \  
libncurses5-dev \  
libpcre3-dev \  
libssl-dev \  
perl \  
make \  
logrotate  
  
RUN curl --location http://openresty.org/download/$FILENAME \--output
/tmp/$FILENAME && \  
tar xzvf /tmp/$FILENAME \--directory=/tmp && \  
cd /tmp/$FULLNAME && \  
./configure --with-http_stub_status_module -j2 && \  
make && \  
make install && \  
make clean && \  
cd /tmp && \  
rm -rf /tmp/$FULLNAME*  
  
RUN mkdir \  
/usr/local/openresty/nginx/sites \  
/usr/local/openresty/nginx/passwd  
  
ENV PATH /usr/local/openresty/nginx/sbin:$PATH  
  
COPY openresty_logrotate.conf /etc/logrotate.d/openresty  
COPY mime.types /usr/local/openresty/nginx/conf/mime.types  
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

