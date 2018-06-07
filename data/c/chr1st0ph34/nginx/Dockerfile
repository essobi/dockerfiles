FROM nginx:1.13.5-alpine  
  
MAINTAINER Euphorika Communications UG (haftungsbeschränkt)
<hello@markenbegeisterung.de>  
  
  
ADD project.conf /etc/nginx/conf.d/project.conf  
ADD shopware.conf /etc/nginx/global/shopware.conf  
  
ADD run.sh /run.sh  
  
RUN chmod 755 /run.sh  
  
CMD ["nginx", "-g", "daemon off;"]

