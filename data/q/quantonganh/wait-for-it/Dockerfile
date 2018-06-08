FROM alpine:3.7  
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-
it.sh /wait-for-it.sh  
  
RUN apk add --no-cache bash  
  
RUN chmod +x /wait-for-it.sh  
  
ENTRYPOINT ["/wait-for-it.sh"]  

