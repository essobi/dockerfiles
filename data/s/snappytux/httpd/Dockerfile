FROM httpd:latest  
MAINTAINER snappy.kop@gmail.com (snappytux.com)  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Change DocumentRoot to /var/www/html  
COPY httpd.conf /usr/local/apache2/conf/  
  
ENV WWW_DIR /var/www/html  
RUN mkdir -p $WWW_DIR \  
&& chown www-data:www-data $WWW_DIR  
  
WORKDIR $WWW_DIR  
RUN touch index.html \  
&& echo "<h1>It's work by snappytux.com</h1>" > index.html  

