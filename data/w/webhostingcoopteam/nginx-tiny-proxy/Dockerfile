FROM nginx:alpine  
  
ENV WHC_NGINX 20170423  
RUN apk update && \  
apk upgrade && \  
apk add openssl && \  
apk add bash && \  
rm -rf /var/cache/apk/*  
  
COPY nginx /assets  
CMD ["/assets/start.sh"]  

