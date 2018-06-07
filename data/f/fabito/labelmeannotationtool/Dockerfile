FROM httpd:2.4-alpine  
  
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
echo '@community http://nl.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories && \  
  
# Install common packages  
apk add \--update \  
perl-cgi-fast \  
make && \  
  
# Install PHP packages  
apk add \--update \  
php5 \  
php5-fpm  
  
ENV LM_TOOL_HOME /usr/src/app/  
  
COPY . /usr/src/app  
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf  
RUN cd /usr/src/app && make

