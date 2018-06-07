FROM nginx:alpine  
  
RUN apk add --update --no-cache \  
openssl  
  
COPY generate_self_signed_ssl.sh /usr/local/bin/generate_self_signed_ssl.sh  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 443  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]

