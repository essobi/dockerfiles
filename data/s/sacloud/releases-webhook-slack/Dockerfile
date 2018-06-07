FROM almir/webhook:2.6.6  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
LABEL MAINTAINER 'Kazumichi Yamamoto <yamamoto.febc@gmail.com>'  
  
RUN apk add --update --no-cache docker  
  
ADD hooks.json.tpl /webhook/slack/conf/  
ADD startup.sh /  
ENTRYPOINT ["/startup.sh"]  

