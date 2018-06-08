FROM swenchancn/alpine:edge  
MAINTAINER SwenChan <a274979395@163.com>  
  
RUN apk upgrade --update && apk add --no-cache mongodb --repository
http://mirrors.aliyun.com/alpine/edge/testing  
  
VOLUME /data/db  
VOLUME /mongodb/log  
  
ENV AUTH=yes \  
STORAGE_ENGINE=wiredTiger \  
JOURNALING=yes  
  
ADD run.sh /run.sh  
ADD init_db.sh /init_db.sh  
  
EXPOSE 27017 28017  
CMD ["/run.sh"]  

