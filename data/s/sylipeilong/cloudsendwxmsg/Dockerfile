FROM mhart/alpine-node  
MAINTAINER lipeilong <xxx@xxx.cn>  
  
ENV TZ=Asia/Shanghai  
RUN apk --update add tzdata && cp /usr/share/zoneinfo/$TZ /etc/localtime &&
echo $TZ > /etc/timezone && \  
apk del tzdata  
  
ADD app /app  
WORKDIR /app  
ENTRYPOINT node app.js $httpHostName $host $user $password $database  
CMD bash

