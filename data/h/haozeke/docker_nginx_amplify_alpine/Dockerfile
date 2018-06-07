# Start with nginx  
FROM nmhung1210/nginx-alpine-amplify  
  
# By Rohit Goswami  
LABEL maintainer="Rohit Goswami <rohit.1995@mail.ru>"  
RUN apk update && apk add git  
  
COPY getOrganizr.sh /bin/  
RUN getOrganizr.sh  
RUN chmod -R 777 /www  
RUN mkdir /config  
RUN chmod -R 777 /config  
  
VOLUME /www /config

