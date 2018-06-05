FROM nginx:alpine  
  
#set the timezone  
RUN apk --no-cache add tzdata && \  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone  
  
COPY conf /etc/nginx/  

