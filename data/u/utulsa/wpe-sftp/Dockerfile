FROM alpine:3.5  
RUN apk update && apk add --no-cache openssh sshpass bash  
ADD script.sh /app/script.sh  
WORKDIR app  
ENTRYPOINT ["/app/script.sh"]  

