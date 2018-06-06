FROM danlynn/ember-cli:2.16.2-node_6.11 as builder  
MAINTAINER Balkrishna Pandey  
  
WORKDIR /root/  
COPY . .  
RUN npm install  
RUN npm install -g bower  
RUN bower install --allow-root  
RUN ember build --environment production  
  
FROM nginx  
  
COPY kubernetes/images/frontend/conf/nginx.conf /etc/nginx/nginx.conf  
COPY kubernetes/images/frontend/conf/frontend.conf
/etc/nginx/conf.d/default.conf  
COPY kubernetes/images/frontend/conf/gzip.conf /etc/nginx/conf.d/gzip.conf  
  
RUN mkdir /var/www  
  
COPY \--from=builder /root/dist/ /var/www  
  
COPY kubernetes/images/frontend/docker-entrypoint.sh /usr/local/bin  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]

