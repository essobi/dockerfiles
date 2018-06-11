FROM nginx:latest  
  
MAINTAINER Liu Chong <mail@clojure.cn>  
  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install --no-install-recommends -y apache2-utils && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD nginx.conf /etc/nginx/conf.d/default.conf  
  
ADD start /usr/local/bin/start  
  
CMD ["start"]  

