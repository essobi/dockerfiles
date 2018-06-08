FROM nginx:1.11-alpine  
  
MAINTAINER Soloman Weng "soloman1124@gmail.com"  
ENV REFRESHED_AT 2016-05-28  
ENV PORT 80  
ENV APP_SERVER app:5000  
COPY nginx.conf.template /etc/nginx/conf.d/default.conf.template  
COPY run.sh /run.sh  
  
CMD ["/run.sh"]  

