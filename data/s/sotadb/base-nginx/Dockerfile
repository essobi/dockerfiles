# We use alpine as the base, with nginx as a web front-end  
FROM alpine:3.5  
ENV LANG en_US.UTF-8  
COPY root /  
ARG FEATURES="nginx"  
#ARG BUILDDEPS=""  
ARG buildversion=none  
  
#RUN apk --update add --no-cache --virtual .build-deps $BUILDDEPS \  
# && apk --update add --no-cache $FEATURES \  
RUN apk --update add --no-cache $FEATURES \  
&& chown -R nginx:nginx /var/www #\  
# && apk del .build-deps  
  
EXPOSE 80 443  
ENTRYPOINT ["/sbin/nginx-prep.sh"] # put env vars into nginx.conf  
CMD ["nginx", "-c", "/etc/nginx/nginx.conf"]  

