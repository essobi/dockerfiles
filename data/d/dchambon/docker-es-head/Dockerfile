FROM nginx:1.10.2-alpine  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash git vim && \  
rm -rf /usr/share/nginx/html/* && \  
git clone git://github.com/mobz/elasticsearch-head.git /usr/share/nginx/html/
&& \  
sed -i 's,http://localhost:9200,http://elasticsearch:9200,'
/usr/share/nginx/html/_site/app.js  
  
COPY docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["nginx"]  

