FROM nginx:1.13.8-alpine  
MAINTAINER EqO_sk  
  
ENV LANG C.UTF-8  
RUN apk add --update openssl  
  
RUN rm -rf /etc/nginx/conf.d/*  
COPY etc/nginx/ /etc/nginx/  
  
RUN rm -rf /usr/share/nginx/html/*  
COPY usr/share/nginx/html/ /usr/share/nginx/html/  
  
COPY req.conf /req.conf  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["nginx"]  

