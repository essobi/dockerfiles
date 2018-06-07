FROM icyleafcn/alpine:latest  
MAINTAINER icyleaf <icyleaf.cn@gmail.com>  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN apk --update --no-cache add bash pwgen su-exec tzdata mysql mysql-client
&& \  
mkdir /run/mysqld && \  
chmod 777 /run/mysqld && \  
chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD [ "mysqld" ]

