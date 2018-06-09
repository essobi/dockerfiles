FROM alpine:3.4  
MAINTAINER pkulakovsky@gmail.com  
  
RUN apk update \  
&& apk add git  
  
ADD repo-sync-setup.sh /  
RUN chmod 700 /repo-sync-setup.sh  
  
RUN mkdir /www-data  
  
WORKDIR /www-data  
  
ENTRYPOINT ["/repo-sync-setup.sh"]

