# dockerfile to create mysql instance using alpine #  
FROM alpine:3.4  
MAINTAINER Shaun Einolf  
# add community edge repository to get php7 packages #  
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/community/' >>
/etc/apk/repositories  
  
# update the os #  
RUN apk update  
  
RUN apk add mariadb \  
mariadb-client  
  
ADD run.sh /usr/sbin  
  
RUN chmod 777 /usr/sbin/run.sh  
  
EXPOSE 3306  
ENTRYPOINT ["/usr/sbin/run.sh"]

