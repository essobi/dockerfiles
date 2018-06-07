FROM almir/webhook:2.6.6  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
LABEL MAINTAINER 'Kazumichi Yamamoto <yamamoto.febc@gmail.com>'  
  
RUN apk add --update --no-cache docker  
  
ADD hooks.json /webhook/dockerhub/conf/  
ADD deploy.sh /webhook/dockerhub/script/  

