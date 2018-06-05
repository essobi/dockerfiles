FROM alpine  
MAINTAINER Daniel Huckstep <darkhelmet@darkhelmetlive.com>  
  
RUN apk --no-cache add nginx  
  
COPY public /yardstick/html  
COPY nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80  
CMD nginx  

