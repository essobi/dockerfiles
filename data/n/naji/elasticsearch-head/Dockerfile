#  
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#  
FROM mobz/elasticsearch-head:5 as builder  
  
FROM nginx:1.13-alpine  
  
WORKDIR /usr/share/nginx/html  
  
COPY \--from=builder /usr/src/app/_site .  
  
COPY default.conf /etc/nginx/conf.d/  
  
COPY docker-entrypoint.sh /usr/local/bin  
  
ENTRYPOINT [ "docker-entrypoint.sh" ]  
  
CMD ["nginx", "-g", "daemon off;"]  

