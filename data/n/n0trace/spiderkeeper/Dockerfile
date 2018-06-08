FROM python:3.6-alpine  
MAINTAINER n0trace,<n0trace@protonmail.com>  
RUN apk update &&\  
apk add tzdata --no-cache &&\  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\  
echo "Asia/Shanghai" > /etc/timezone  
RUN pip install --no-cache-dir spiderkeeper  
EXPOSE 5000 6800  
CMD ["spiderkeeper"]

