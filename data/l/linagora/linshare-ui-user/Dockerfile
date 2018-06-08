from httpd:2.4  
MAINTAINER LinShare <linshare@linagora.com>  
  
ARG VERSION="2.1.1"  
ARG CHANNEL="releases"  
ARG EXT="com"  
RUN apt-get update && apt-get install wget bzip2 -y && apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN
URL="https://nexus.linagora.${EXT}/service/local/artifact/maven/content?r=linshare-${CHANNEL}&g=org.linagora.linshare&a=linshare-
ui-user&v=${VERSION}"; \  
wget --no-check-certificate --progress=bar:force:noscroll \  
-O ui-user.tar.bz2 "${URL}&p=tar.bz2" && \  
wget --no-check-certificate --progress=bar:force:noscroll \  
-O ui-user.tar.bz2.sha1 "${URL}&p=tar.bz2.sha1" && \  
sed -i 's#^\\(.*\\)#\1\tui-user.tar.bz2#' ui-user.tar.bz2.sha1 && \  
sha1sum -c ui-user.tar.bz2.sha1 --quiet && rm -f ui-user.tar.bz2.sha1  
  
RUN tar -jxf ui-user.tar.bz2 -C /usr/local/apache2/htdocs && \  
chown -R www-data /usr/local/apache2/htdocs/linshare-ui-user && \  
rm -f ui-user.tar.bz2  
  
RUN sed -i 's/^\\(devMode:\\).*/\1 false/' /usr/local/apache2/htdocs/linshare-
ui-user/scripts/config.js && \  
sed -i 's/^\\(production:\\).*/\1 true/' /usr/local/apache2/htdocs/linshare-
ui-user/scripts/config.js  
  
COPY ./httpd.extra.conf /usr/local/apache2/conf/extra/httpd.extra.conf  
RUN cat /usr/local/apache2/conf/extra/httpd.extra.conf >>
/usr/local/apache2/conf/httpd.conf  
  
COPY ./linshare-ui-user.conf /usr/local/apache2/conf/extra/linshare-ui-
user.conf  
  
EXPOSE 80  

