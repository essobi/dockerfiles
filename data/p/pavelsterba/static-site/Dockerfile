FROM alpine  
MAINTAINER Pavel Sterba "email@pavelsterba.com"  
COPY data/nginx.conf /etc/nginx/nginx.conf  
  
RUN apk update && apk upgrade \  
&& apk add nginx bash \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 80  
CMD ["nginx"]  

