FROM alpine:3.3  
RUN apk update && \  
apk add -u ca-certificates  
  
ADD heapster /heapster  
  
EXPOSE 8082  
CMD ["/heapster"]  

