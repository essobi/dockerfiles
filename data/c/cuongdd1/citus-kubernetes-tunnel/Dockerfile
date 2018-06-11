FROM nginx:alpine  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
ENV AWS_ACCESS_KEY_ID=  
ENV AWS_SECRET_ACCESS_KEY=  
ENV AWS_DEFAULT_REGION=ap-northeast-1  
VOLUME /root/  
  
RUN apk -Uuv add curl && \  
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && \  
mv ./kubectl /usr/local/bin/kubectl && \  
apk --purge -v del curl && \  
rm /var/cache/apk/*  
  
ADD filesystem /  
  
COPY docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 8020  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]

