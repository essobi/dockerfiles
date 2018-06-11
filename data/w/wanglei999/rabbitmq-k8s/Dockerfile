FROM rabbitmq:3.6-management-alpine  
  
MAINTAINER edwinlll  
  
RUN apk update && apk add ca-certificates && apk add tzdata && ln -sf
/usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo Asia/Shanghai >
/etc/timezone  
  
ADD plugins/*.ez /opt/rabbitmq/plugins/  
RUN rabbitmq-plugins enable \--offline autocluster  

