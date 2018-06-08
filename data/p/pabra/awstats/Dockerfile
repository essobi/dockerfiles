FROM httpd:2.4.33-alpine  
  
ENV AWSTATS_VERSION 7.6-r2  
  
RUN apk add --no-cache awstats=${AWSTATS_VERSION} gettext \  
&& echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories \  
&& apk add --no-cache apache2-mod-perl \  
&& echo 'Include conf/awstats_httpd.conf' >>
/usr/local/apache2/conf/httpd.conf  
  
ADD awstats_env.conf /etc/awstats/  
ADD awstats_httpd.conf /usr/local/apache2/conf/  
ADD entrypoint.sh /usr/local/bin/  
  
ENV AWSTATS_CONF_LOGFILE "/var/local/log/access.log"  
ENV AWSTATS_CONF_LOGFORMAT "%host %other %logname %time1 %methodurl %code
%bytesd %refererquot %uaquot"  
ENV AWSTATS_CONF_SITEDOMAIN "my_website"  
ENV AWSTATS_CONF_HOSTALIASES "localhost 127.0.0.1 REGEX[^.*$]"  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["httpd-foreground"]  

