FROM node:alpine  
  
RUN apk --no-cache add \  
git  
  
RUN mkdir /data  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["git"]  
CMD ["pull"]

