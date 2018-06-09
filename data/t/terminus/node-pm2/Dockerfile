FROM node:8.9.4-alpine  
  
# Set special timezone  
RUN export TZ="Asia/Shanghai" && \  
echo "http://mirrors.aliyun.com/alpine/v3.6/main/" > /etc/apk/repositories &&
\  
echo "http://mirrors.aliyun.com/alpine/v3.6/community/" >>
/etc/apk/repositories && \  
apk add --no-cache tzdata && \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo $TZ > /etc/timezone && \  
rm -fr /var/cache/apk/*  
  
RUN npm i -g pm2@2.1.6  

