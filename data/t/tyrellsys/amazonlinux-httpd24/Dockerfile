FROM amazonlinux:2016.09  
ENV PCRE_VERSION 8.40  
ENV OPENSSL_VERSION 1.0.2k  
ENV APACHE_VERSION 2.4.25  
ENV APR_VERSION 1.5.2  
ENV APRU_VERSION 1.5.4  
RUN yum -y update && yum -y install wget gcc gcc-c++ perl zlib-devel findutils
diffutils file  
  
# Download, configure and install PCRE  
RUN wget -O - https://ftp.pcre.org/pub/pcre/pcre-"${PCRE_VERSION}".tar.gz | \  
tar -xzf - -C /tmp && \  
cd /tmp/pcre-"${PCRE_VERSION}" && \  
./configure --prefix=/opt/pcre/pcre-"${PCRE_VERSION}" && make && make install  
  
# Download, configure and install OpenSSL  
RUN wget -O -
https://www.openssl.org/source/openssl-"${OPENSSL_VERSION}".tar.gz | \  
tar -xzf - -C /tmp && \  
cd /tmp/openssl-"${OPENSSL_VERSION}" && \  
./config --prefix=/opt/openssl/openssl-"${OPENSSL_VERSION}" shared zlib &&
make && make install  
  
# Download, configure and install Apache  
RUN wget -O - http://www-
us.apache.org/dist/httpd/httpd-"${APACHE_VERSION}".tar.gz | \  
tar -xzf - -C /tmp && \  
cd /tmp/httpd-"${APACHE_VERSION}" && \  
wget -O - http://www-us.apache.org/dist/apr/apr-"${APR_VERSION}".tar.gz | \  
tar -xzf - -C ./srclib && \  
mv ./srclib/apr-"${APR_VERSION}" ./srclib/apr && \  
wget -O - http://www-us.apache.org/dist//apr/apr-util-"${APRU_VERSION}".tar.gz
| \  
tar -xzf - -C ./srclib && \  
mv ./srclib/apr-util-"${APRU_VERSION}" ./srclib/apr-util && \  
./configure \  
\--prefix=/opt/httpd/httpd-"${APACHE_VERSION}" \  
\--sbindir=/usr/local/sbin \  
\--with-ssl=/opt/openssl/openssl-"${OPENSSL_VERSION}" \  
\--enable-ssl \  
\--enable-ssl-staticlib-deps \  
\--enable-mods-static=ssl \  
\--enable-proxy \  
\--with-included-apr \  
\--with-pcre=/opt/pcre/pcre-"${PCRE_VERSION}" && \  
make && make install  
  
# Clean up unnecessary artifacts  
WORKDIR /opt/httpd/httpd-"${APACHE_VERSION}"/conf  
RUN rm -rf /tmp/httpd-"${APACHE_VERSION}" && \  
rm -rf /tmp/openssl-"${OPENSSL_VERSION}" && \  
rm -rf /tmp/pcre-"${PCRE_VERSION}"  
  
# Add extra configuration  
RUN { echo 'ServerName localhost'; \  
echo 'LoadModule slotmem_shm_module modules/mod_slotmem_shm.so'; \  
echo 'LoadModule socache_shmcb_module modules/mod_socache_shmcb.so'; \  
} >> ./httpd.conf  
  
# Add ld.so.conf  
RUN echo "/opt/openssl/openssl-${OPENSSL_VERSION}/lib" >
/etc/ld.so.conf.d/openssl.conf && ldconfig  
  
# Define default command  
CMD ["apachectl", "-D", "FOREGROUND"]  
  
# Expose ports  
EXPOSE 80 443  

