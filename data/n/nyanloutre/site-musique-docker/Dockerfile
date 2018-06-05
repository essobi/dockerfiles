FROM nginx:1.11.4-alpine  
MAINTAINER Paul TREHIOU <paul.trehiou@gmail.com>  
  
RUN \  
apk \--no-cache add curl tar && \  
rm -rf /usr/share/nginx/html/* && \  
  
# Installing Piwik  
mkdir -p /usr/share/nginx/html/analytics && \  
curl -sL \--retry 3 https://builds.piwik.org/piwik-3.0.1.tar.gz \  
| gunzip \  
| tar x -C /usr/share/nginx/html/analytics \--strip-components=1 &&\  
chmod 777 /usr/share/nginx/html/analytics/tmp && \  
chmod 777 /usr/share/nginx/html/analytics/config && \  
chmod 777 /usr/share/nginx/html/analytics/misc/user && \  
mv /usr/share/nginx/html/analytics/config
/usr/share/nginx/html/analytics/config.old  
# Configure Nginx  
COPY nginx-site.conf /etc/nginx/conf.d/default.conf  

