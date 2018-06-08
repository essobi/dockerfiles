FROM node:9.10.1-alpine  
  
RUN apk update && apk add git python  
  
COPY ./script.sh /  
RUN chmod +x /script.sh  
  
CMD ["/script.sh"]

