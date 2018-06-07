FROM alpine:3.6  
LABEL docker run --rm frontendwordpress/dongnelibrary dongnelibrary -l 여주도서관
-t 자바  
  
RUN apk update && \  
apk add nodejs-npm && \  
npm install dongnelibrary -g && \  
rm /var/cache/apk/*  
  
#CMD ["dongnelibrary"]  

