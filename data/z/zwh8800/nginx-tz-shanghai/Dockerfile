FROM nginx:alpine  
RUN apk update && apk add tzdata && \  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone  
  

