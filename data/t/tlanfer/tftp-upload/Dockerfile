FROM alpine  
RUN apk update && apk add tftp-hpa  
ADD upload.sh /  
ENTRYPOINT [ "/upload.sh" ]  

