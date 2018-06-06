FROM httpd:2.4  
MAINTAINER Dang Mai <contact@dangmai.net>  
  
COPY . /src  
  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
bzip2 \  
libfreetype6 \  
libfontconfig \  
&& curl -sL https://deb.nodesource.com/setup_5.x | bash \  
&& apt-get install -y nodejs \  
&& sed -i '/<Directory "\/usr\/local\/apache2\/htdocs">/,/<\/Directory>/
s/AllowOverride None/AllowOverride All/' /usr/local/apache2/conf/httpd.conf \  
&& sed -i 's/#LoadModule rewrite_module/LoadModule rewrite_module/'
/usr/local/apache2/conf/httpd.conf \  
&& rm -rf /usr/local/apache2/htdocs/* \  
&& cd /src \  
&& npm install \  
&& npm test \  
&& npm run build \  
&& cp -aR ./www-built/. /usr/local/apache2/htdocs/ \  
&& rm -rf /src \  
&& apt-get remove -y --purge \  
nodejs \  
bzip2 \  
curl \  
libfreetype6 \  
libfontconfig \  
&& apt-get autoremove -y \  
&& apt-get clean  
  
EXPOSE 80  

