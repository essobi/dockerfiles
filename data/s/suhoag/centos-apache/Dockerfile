FROM centos:5.11  
MAINTAINER Haesung Hwang <suhoag@naver.com>  
  
RUN rm -f /etc/yum.repos.d/*  
ADD yum.repos.d/CentOS-Vault.repo /etc/yum.repos.d/CentOS-Vault.repo  
  
RUN yum -y update && yum -y install gcc make wget openssl-devel gcc-c++ && yum
-y clean all  
  
ENV HTTPD_PREFIX /usr/local/apache  
RUN mkdir -p "$HTTPD_PREFIX"  
  
WORKDIR "$HTTPD_PREFIX"  
  
# apr install  
RUN mkdir -p src \  
&& cd src \  
&& wget -O apr.tar.gz
"https://www.apache.org/dyn/closer.cgi?action=download&filename=apr/apr-1.5.2.tar.gz"
\--no-check-certificate \  
&& mkdir apr \  
&& tar -xvf apr.tar.gz -C apr --strip-components=1 \  
&& cd apr \  
&& ./configure \  
&& make && make install \  
&& cd ..  
  
# apr-util install  
RUN wget -O apr-util.tar.gz
"https://www.apache.org/dyn/closer.cgi?action=download&filename=apr/apr-
util-1.5.4.tar.gz" \--no-check-certificate \  
&& mkdir apr-util \  
&& tar -xvf apr-util.tar.gz -C apr-util --strip-components=1 \  
&& cd apr-util \  
&& ./configure --with-apr="/usr/local/apr" \  
&& make && make install \  
&& cd ..  
  
# pcre install  
RUN wget -O pcre.tar.gz
ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.40.tar.gz \  
&& mkdir pcre \  
&& tar -xvf pcre.tar.gz -C pcre --strip-components=1 \  
&& cd pcre \  
&& ./configure \  
&& make && make install \  
&& cd ..  
  
# httpd install  
RUN wget -O httpd.tar.gz
"https://www.apache.org/dyn/closer.cgi?action=download&filename=httpd/httpd-2.4.25.tar.gz"
\--no-check-certificate \  
&& mkdir httpd \  
&& tar -xvf httpd.tar.gz -C httpd --strip-components=1 \  
&& cd httpd \  
&& ./configure --prefix="/usr/local/apache" \--with-apr="/usr/local/apr"
\--enable-mods-shared=most --enable-ssl \  
&& make && make install \  
&& cd "$HTTPD_PREFIX" \  
&& rm -fr src man manual  
  
EXPOSE 80

