FROM openfrontier/gerrit  
  
MAINTAINER ravih <ravi.huang@gmail.com>  
  
COPY fcgi-run /etc/init.d/  
COPY spawn-fcgi /usr/bin/  
COPY start_nginx.sh /docker-entrypoint-init.d/  
COPY gerrit-entrypoint.sh /  
  
RUN apk add nginx apache2-utils fcgi fcgiwrap && \  
htpasswd -bc /etc/nginx/users admin passwd && \  
sed -i "s/\/pub\/git/\/var\/gerrit\/review_site\/git/g"
/usr/share/gitweb/gitweb.cgi && \  
git config \--global core.quotepath false && \  
git config \--global i18n.logoutputencoding utf8 && \  
git config \--global i18n.commitencoding utf8 && \  
chmod +x /gerrit-entrypoint.sh && \  
chmod +x /etc/init.d/fcgi-run && \  
chmod +x /usr/bin/spawn-fcgi  
  
COPY nginx.conf /etc/nginx/  

